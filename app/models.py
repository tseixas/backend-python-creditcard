from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates
import datetime
import calendar
import pytz
from fastapi import HTTPException


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    exp_date = Column(DateTime)
    holder = Column(String)
    number = Column(String)
    cvv = Column(Integer)
    brand = Column(String)

    @validates("exp_date")
    def validate_exp_date(self, key, exp_date):
        timezone = pytz.timezone('UTC')

        if exp_date.replace(tzinfo=timezone) < datetime.datetime.now().replace(tzinfo=timezone):
            raise HTTPException(
                status_code=400, detail="failed simple exp_date validation")

        year = exp_date.year
        month = exp_date.month

        _, last_day = calendar.monthrange(year, month)
        exp_date = datetime.datetime(year, month, last_day)

        return exp_date

    @validates("holder")
    def validate_holder(self, key, holder):
        if len(holder) < 2:
            raise HTTPException(
                status_code=400, detail="failed simple holder validation")

        return holder

    @validates("cvv")
    def validate_cvv(self, key, cvv):
        cvv = str(cvv)

        if len(cvv) < 3 or len(cvv) > 4:
            raise HTTPException(
                status_code=400, detail="failed simple cvv validation")

        return cvv
