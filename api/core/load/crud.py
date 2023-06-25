import os.path as path
import sys
two_up =  path.abspath(path.join(__file__ ,"../.."))
sys.path.append(two_up)

from sqlalchemy.orm import Session
from schema import currencyInformation, currencyHistory
from models import Crypto

def insert_crypto_information(db: Session, crypto: Crypto):
    currency_information = currencyInformation(pair = crypto.name, exchange="OKX")
    db.add(currency_information)
    db.commit()
    db.refresh(currency_information)
    return currency_information

def insert_crypto_history(db: Session, crypto: Crypto):
    currency_history = currencyHistory(pair = crypto.name, time_range=crypto.current_time,
                                           timestamp = crypto.timestamp, open_price = crypto.open_price,
                                           high_price = crypto.high_price, low_price = crypto.low_price,
                                           close_price = crypto.close_price, derivatives_volume = crypto.derivatives_volume,
                                           trading_volume = crypto.trading_volume)
    db.add(currency_history)
    db.commit()
    db.refresh(currency_history)
    return currency_history




def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

