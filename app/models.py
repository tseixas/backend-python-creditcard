from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates
import datetime
import calendar
import pytz


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    exp_date = Column(DateTime)
    holder = Column(String)
    number = Column(String)
    cvv = Column(Integer)

    @validates("exp_date")
    def validate_exp_date(self, key, exp_date):
        if exp_date.replace(tzinfo=pytz.timezone('UTC')) < datetime.datetime.now().replace(tzinfo=pytz.timezone('UTC')):
            raise ValueError("failed simple exp_date validation")

        year = exp_date.year
        month = exp_date.month

        _, last_day = calendar.monthrange(year, month)
        exp_date = datetime.datetime(year, month, last_day)

        return exp_date

    @validates("holder")
    def validate_holder(self, key, holder):
        if len(holder) < 2:
            raise ValueError("failed simple holder validation")

        return holder

    @validates("cvv")
    def validate_cvv(self, key, cvv):
        cvv = str(cvv)

        if len(cvv) < 3 or len(cvv) > 4:
            raise ValueError("failed simple cvv validation")

        return cvv
