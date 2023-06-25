import requests
import pandas as pd
from datetime import datetime



class get_currency_ticker():
    
    def __init__(self,timestamp = "15m",currency_list=["BTC-USDT"]):
        self._timestamp = timestamp,
        self._currency_list = currency_list
        self._url = 'https://www.okx.com',
        self._endpoint = 'https://www.okx.com'
        self._results = pd.DataFrame(columns=["unixTimestamp", "Open Price", "High Price","Low Price", "Close Price", "Derivatives Volume", "Trading Volume", "volCcyQuote", "isCompleted","currency"])
        get_currency_ticker()
        
    def get_results(self):
        return self._results
    
    def get_currency_ticker(timestamp="15m", currency="BTC-USDT"):
        params = {"bar":timestamp, "instId":currency}
        ticker = pd.DataFrame(requests.get(url + endpoint, params=params).json()['data'])
        ticker.columns = ["unixTimestamp", "Open Price", "High Price","Low Price", "Close Price", "Derivatives Volume", "Trading Volume", "volCcyQuote", "isCompleted"]
        for timestamp in range(len(ticker['unixTimestamp'])):
            ticker['unixTimestamp'][timestamp] = datetime.utcfromtimestamp(int(ticker['unixTimestamp'][timestamp])/1000).strftime('%Y-%m-%d %H:%M:%S')        
        ticker['currency'] = currency
        return ticker
    
    def get_currencies_ticker(self):
        for inst in self._currency_list:
            _result = self.get_currencies_ticker(currency=inst)
            self._results = pd.concat([_result, self._results], ignore_index=True)            