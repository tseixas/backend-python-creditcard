from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm

from fastapi_sqlalchemy import DBSessionMiddleware

from app.database import DATABASE_URL, engine
from app.v1.cards.actions import save_card, get_card_by_id, get_cards
from app.auth.actions import token

from app.domain import schemas, models

from app.auth.actions import get_current_active_user


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Credit Card")

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL,
                   custom_engine=engine)


@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return token(form_data)


@app.post('/api/v1/credit-card/', response_model=schemas.Card)
def create_card(card: schemas.CardBase, current_user: schemas.User = Depends(get_current_active_user)):
    return save_card(card=card)


@app.get('/api/v1/credit-card/', response_model=schemas.CardList)
def list_cards(skip: int = 0, limit: int = 10, page: int = 1, current_user: schemas.User = Depends(get_current_active_user)):
    return get_cards(skip=skip, limit=limit, page=page)


@app.get('/api/v1/credit-card/{card_id}', response_model=schemas.Card)
def get_card(card_id: int, current_user: schemas.User = Depends(get_current_active_user)):
    return get_card_by_id(card_id=card_id)
