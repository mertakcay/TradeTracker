import os.path as path
import sys
two_up =  path.abspath(path.join(__file__ ,"../.."))
sys.path.append(two_up)

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from models.extract import Crypto
from schemas import load
from sqlalchemy.orm import Session

from adapter.api.okx import currencyTicker
from utils.sqlalchemy import engine
from utils.dependencies import get_db

from core.load import crud

currency_ticker = None

load.Base.metadata.create_all(bind=engine)
extract_router = APIRouter()


@extract_router.on_event("startup")
async def startup_event():
    global currency_ticker
    currency_ticker = currencyTicker()
    


@extract_router.get("/crypto",response_model=list[Crypto], tags=["okx"])
async def get_all_crypt(db: Session = Depends(get_db)):
    global currency_ticker
    results = currency_ticker.get_currencies_ticker()
    crud.insert_crypto_information(db,crypto=results)
    return results

@extract_router.get("/crypto/{currency_pair}",response_model=Crypto, tags=["okx"])
async def get_all_crypt(currency_pair, db: Session = Depends(get_db)):
    global currency_ticker
    print(currency_pair)
    results = currency_ticker.get_currency_ticker(currency = currency_pair)
    return results


