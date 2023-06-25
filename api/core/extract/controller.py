import os.path as path
import sys
two_up =  path.abspath(path.join(__file__ ,"../.."))
sys.path.append(two_up)

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .models import Crypto

from adapter.api.okx import currencyTicker
from utils.sqlalchemy import SessionLocal, engine
from utils.dependencies import get_db

extract_router = APIRouter()


@extract_router.get("/crypto",response_model=list[Crypto], tags=["okx"])
async def get_all_crypt():
    results = currencyTicker.get_results()
    return results

@extract_router.get("/crypto/{currency_pair}",response_model=Crypto, tags=["okx"])
async def get_all_crypt(currency_pair):
    print(currency_pair)
    results = currencyTicker().get_currency_ticker(currency = currency_pair)
    return results


