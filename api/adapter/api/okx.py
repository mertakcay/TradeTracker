import os.path as path
import sys
two_up =  path.abspath(path.join(__file__ ,"../.."))
sys.path.append(two_up)

import requests
import pandas as pd
from models.extract import Crypto, cryptoHistory
from datetime import datetime



class currencyTicker(object):
    
    def __init__(self,timestamp = "15m",currency_list=["BTC-USDT"], time_range=2):
        self._timestamp = timestamp
        self._currency_list = currency_list
        self._time_ramge = time_range
        self._url = 'https://www.okx.com'
        self._endpoint = "/api/v5/market/candles"
        
        
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
        
        history = list()
        for idx, tick in ticker.iterrows():
            
            crypto_history = cryptoHistory(timestamp = tick['unixTimestamp'],
                            open_price = tick['Open Price'], high_price = tick['High Price'],
                            low_price = tick['Low Price'], close_price = tick['Close Price'],
                            derivatives_volume = tick['Derivatives Volume'], trading_volume = tick['Trading Volume'],
                            complete = tick["isCompleted"])
            
            history.append(crypto_history)
            
        crypto = Crypto(name = currency, current_time = self._timestamp, crypto_history = history)

        return crypto
    
    def get_currencies_ticker(self):
        _results = list()
        for currency in self._currency_list:
            _result = self.get_currency_ticker(currency=currency)
            _results.append(_result)  
        return _results        