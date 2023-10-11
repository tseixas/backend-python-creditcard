from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from typing import List
from . import actions, models, schemas
from pydantic import BaseModel
from app.database import DATABASE_URL, engine
from fastapi_sqlalchemy import DBSessionMiddleware


app = FastAPI(title="Credit Card")

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL, custom_engine=engine)

class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }


class Message(BaseModel):
    message: str


@app.post("/cards/", response_model=schemas.Card)
def create_card(card: schemas.Card):
    return actions.save_card(card=card)


@app.get("/cards/", response_model=List[schemas.Card])
def read_cards(skip: int = 0, limit: int = 10):
    return actions.get_cards(skip=skip, limit=limit)


@app.get("/cards/{card_id}", response_model=schemas.Card, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
def read_card(card_id: int):
    return actions.get_card_by_id(card_id=card_id)
