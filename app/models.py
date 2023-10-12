from .database import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import validates
import datetime
import calendar
import pytz
from fastapi import HTTPException


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    exp_date = Column(Date)
    holder = Column(String)
    number = Column(String)
    cvv = Column(Integer)
    brand = Column(String)

    @validates("exp_date")
    def validate_exp_date(self, key, exp_date):
        today = datetime.datetime.now().date()

        if exp_date < today:
            raise HTTPException(
                status_code=400, detail="Invalid Expiration date")

        year = exp_date.year
        month = exp_date.month

        _, last_day = calendar.monthrange(year, month)
        exp_date = datetime.datetime(year, month, last_day)

        return exp_date

    @validates("holder")
    def validate_holder(self, key, holder):
        if len(holder) < 2:
            raise HTTPException(
                status_code=400, detail="Invalid Holder")

        return holder

    @validates("cvv")
    def validate_cvv(self, key, cvv):
        cvv = str(cvv)

        if len(cvv) < 3 or len(cvv) > 4:
            raise HTTPException(
                status_code=400, detail="Invalid CVV")

        return cvv
