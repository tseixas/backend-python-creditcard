from fastapi import HTTPException
from fastapi_sqlalchemy import db
from . import models, schemas
from math import ceil
from creditcard import CreditCard


def get_card_by_id(card_id: int):
    card = db.session.query(models.Card).filter(
        models.Card.id == card_id).first()

    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    return card


def get_cards(skip: int = 0, limit: int = 10, page: int = 1):
    if page < 1:
        page = 1

    skip = page * limit

    query = db.session.query(models.Card)

    total = query.count()
    pages = ceil(total / limit)
    result = query.offset(skip).limit(limit).all()

    return {
        "data": result,
        "total": total,
        "pages": pages
    }


def save_card(card: schemas.Card):
    db_card = models.Card(
        exp_date=card.exp_date,
        holder=card.holder,
        number=card.number,
        cvv=card.cvv
    )

    credit_card = CreditCard(card.number)

    if not credit_card.is_valid():
        raise HTTPException(status_code=404, detail="Card inválid")

    credit_card.get_brand()

    db.session.add(db_card)
    db.session.commit()
    db.session.refresh(db_card)

    return db_card
