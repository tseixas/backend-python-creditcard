from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from . import actions, schemas, models
from app.database import DATABASE_URL, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Credit Card")

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL,
                   custom_engine=engine)


@app.post("/cards/", response_model=schemas.Card)
def save_card(card: schemas.Card):
    return actions.save_card(card=card)


@app.get("/cards/", response_model=schemas.CardList)
def list_cards(skip: int = 0, limit: int = 10, page: int = 1):
    return actions.get_cards(skip=skip, limit=limit, page=page)


@app.get("/cards/{card_id}", response_model=schemas.Card)
def get_card(card_id: int):
    return actions.get_card_by_id(card_id=card_id)
