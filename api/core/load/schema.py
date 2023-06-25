import os.path as path
import sys
two_up =  path.abspath(path.join(__file__ ,"../.."))
sys.path.append(two_up)

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float,DateTime
from sqlalchemy.orm import relationship

from utils.sqlalchemy import Base


class currencyInformation(Base):
    __tablename__ = "currency_information"

    pair = Column(String, primary_key=True, index=True)
    exchange = Column(String)
    # first parameter is name of table of db
    # second parameter is created object name of relationship in object
    currencyHistory = relationship("currencyHistory", back_populates="information") 


class currencyHistory(Base):
    __tablename__ = "currency_history"

    id = Column(Integer, primary_key=True, index=True)
    pair = Column(String, ForeignKey( ForeignKey("currency_information.pair")))
    time_range = Column(str)
    timestamp = Column(DateTime)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    derivatives_volume = Column(Float)
    trading_volume = Column(Float)
    # first parameter is name of table of db
    # second parameter is created object name of relationship in object
    information = relationship("currencyInformation", back_populates="currencyHistory")