from pydantic import BaseModel
import datetime


class Card(BaseModel):
    id: int
    exp_date: datetime.datetime
    holder: str
    number: str
    cvv: str

    class Config:
        orm_mode = True
