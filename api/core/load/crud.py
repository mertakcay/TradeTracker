import os.path as path
import sys
two_up =  path.abspath(path.join(__file__ ,"../.."))
sys.path.append(two_up)

from sqlalchemy.orm import Session
from schemas.load import currencyHistory, currencyInformation
from models.load import Crypto

def insert_crypto_information(db: Session, crypto: Crypto):
    for crypto_sample in crypto:
        currency_information = currencyInformation(pair = crypto_sample.name, exchange="OKX")
        db.add(currency_information)
        db.commit()
        db.refresh(currency_information)
        for crypto_sample_history in crypto_sample.crypto_history:
            currency_history = currencyHistory(pair = crypto_sample_history.pair, time_range = crypto_sample.current_time,
                                               timestamp = crypto_sample_history.timestamp, open_price = crypto_sample_history.open_price,
                                               high_price = crypto_sample_history.high_price, low_price = crypto_sample_history.low_price,
                                               close_price = crypto_sample_history.close_price, derivatives_volume = crypto_sample_history.derivatives_volume,
                                               trading_volume = crypto_sample_history.trading_volume, complete = crypto_sample_history.complete)
            db.add(currency_history)
            db.commit()
            db.refresh(currency_history)
            

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

