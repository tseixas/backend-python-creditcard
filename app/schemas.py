from pydantic import BaseModel
import datetime
from typing import List


class Card(BaseModel):
    id: int
    exp_date: datetime.datetime
    holder: str
    number: str
    cvv: int

    class Config:
        from_attributes = True


class CardList(BaseModel):
    total: int
    pages: int
    data: List[Card]

    class Config:
        from_attributes = True
