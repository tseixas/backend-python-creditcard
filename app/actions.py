from fastapi_sqlalchemy import db
from . import models, schemas


def get_card_by_id(card_id: str):
    return db.query(models.Card).filter(models.Card.id == card_id).first()


def get_cards(skip: int = 0, limit: int = 10):
    return db.session.query(models.Card).offset(skip).limit(limit).all()


def save_card(card: schemas.Card):
    db_card = models.Card(
        exp_date=card.exp_date,
        holder=card.holder,
        number=card.number,
        cvv=card.cvv
    )

    db.session.add(db_card)
    db.session.commit()
    db.session.refresh(db_card)

    return db_card
