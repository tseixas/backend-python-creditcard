from datetime import datetime, timedelta
from typing import Annotated, Union

from app.database import DATABASE_URL, engine

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi_sqlalchemy import DBSessionMiddleware

from jose import JWTError, jwt
from passlib.context import CryptContext

from . import actions, schemas, models


SECRET_KEY = "34fc16eb6fd5afaaa9b61aec70e5cef05b80c91f2dc502025b9ed9bd6100d897"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

default_user = {
    "admin": {
        "username": "admin",
        "full_name": "Admin",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    }
}


models.Base.metadata.create_all(bind=engine)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="Credit Card")

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL,
                   custom_engine=engine)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return schemas.UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)

    if not user:
        return False

    if not verify_password(password, user.hashed_password):
        return False

    return user


def fake_decode_token(token):
    return get_user(default_user, token)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(default_user, username=token_data.username)

    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(
    current_user: Annotated[schemas.User, Depends(get_current_user)]
):
    return current_user


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(
        default_user, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@ app.post('/api/v1/credit-card/', response_model=schemas.Card)
def save_card(card: schemas.CardBase, current_user: schemas.User = Depends(get_current_active_user)):
    return actions.save_card(card=card)


@ app.get('/api/v1/credit-card/', response_model=schemas.CardList)
def list_cards(skip: int = 0, limit: int = 10, page: int = 1, current_user: schemas.User = Depends(get_current_active_user)):
    return actions.get_cards(skip=skip, limit=limit, page=page)


@ app.get('/api/v1/credit-card/{card_id}', response_model=schemas.Card)
def get_card(card_id: int, current_user: schemas.User = Depends(get_current_active_user)):
    return actions.get_card_by_id(card_id=card_id)
