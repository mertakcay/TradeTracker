from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class cryptoHistory(BaseModel):
    timestamp: datetime
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    derivatives_volume: float
    trading_volume: float
    complete: bool
    class Config:
        orm_mode = True

class Crypto(BaseModel):
    name: str
    current_time: str 
    crypto_history: list[cryptoHistory]
    
    class Config:
        orm_mode = True





    
    
    

