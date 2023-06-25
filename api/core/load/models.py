from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class Crypto(BaseModel):
    name: str
    current_time: str 
    timestamp: list[datetime]
    open_price: list[float]
    high_price: list[float]
    low_price: list[float]
    close_price: list[float]
    derivatives_volume: list[float]
    trading_volume: list[float]
    complete: list[bool]
    class Config:
        orm_mode = True

    
    
    

