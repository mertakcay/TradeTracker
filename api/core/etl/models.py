from pydantic import BaseModel

class Crypto(BaseModel):
    name: str
    current_time: str 
    open_price: float
    high_price: float 
    low_price: float
    close_price: float
    derivatives_volume: float
    traing_volume: float
    complete: bool