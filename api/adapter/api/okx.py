import os.path as path
import sys
two_up =  path.abspath(path.join(__file__ ,"../.."))
sys.path.append(two_up)

import requests
import pandas as pd
from core.extract.models import Crypto
from datetime import datetime



class currencyTicker():
    
    def __init__(self,timestamp = "15m",currency_list=["BTC-USDT"], time_range=2):
        self._timestamp = timestamp
        self._currency_list = currency_list
        self._time_ramge = time_range
        self._url = 'https://www.okx.com'
        self._endpoint = "/api/v5/market/candles"
        self._results = self.get_currencies_ticker()
        
        
    def get_results(self):
        return self._results
    
    def get_currency_ticker(self, currency):
        params = {"bar":self._timestamp, "instId":currency, "limit":self._time_ramge}
        ticker = pd.DataFrame(requests.get(self._url + self._endpoint, params=params).json()['data'])
        ticker.columns = ["unixTimestamp", "Open Price", "High Price","Low Price", "Close Price", "Derivatives Volume", "Trading Volume", "volCcyQuote", "isCompleted"]
        for timestamp in range(len(ticker['unixTimestamp'])):
            ticker['unixTimestamp'][timestamp] = datetime.utcfromtimestamp(int(ticker['unixTimestamp'][timestamp])/1000).strftime('%Y-%m-%d %H:%M:%S') 
            ticker['unixTimestamp'][timestamp] = datetime.strptime(ticker['unixTimestamp'][timestamp], '%Y-%m-%d %H:%M:%S')
        ticker['Trading Volume'] = pd.to_numeric(ticker['Trading Volume'])
        crypto = Crypto(name = currency, current_time = self._timestamp,timestamp = ticker['unixTimestamp'].to_list(),
                        open_price = ticker['Open Price'].to_list(), high_price = ticker['High Price'].to_list(),
                        low_price = ticker['Low Price'].to_list(), close_price = ticker['Close Price'].to_list(),
                        derivatives_volume = ticker['Derivatives Volume'].to_list(), trading_volume = ticker['Trading Volume'].to_list(),
                        complete = ticker["isCompleted"].to_list())
        print(crypto)
        return crypto
    
    def get_currencies_ticker(self):
        _results = list()
        for currency in self._currency_list:
            _result = self.get_currency_ticker(currency=currency)
            _results.append(_result)  
        return _results        