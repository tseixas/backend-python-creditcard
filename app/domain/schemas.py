from pydantic import BaseModel
import datetime
from typing import List


class User(BaseModel):
    id: int
    username: str
    full_name: str


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class CardBase(BaseModel):
    exp_date: datetime.date
    holder: str
    number: str
    cvv: int

    class Config:
        from_attributes = True


class Card(CardBase):
    id: int
    exp_date: datetime.date
    holder: str
    number: str
    cvv: int
    brand: str

    class Config:
        from_attributes = True


class CardList(BaseModel):
    total: int
    pages: int
    data: List[Card]

    class Config:
        from_attributes = True
