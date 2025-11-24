import requests
import logging

logger = logging.getLogger(__name__)

class MarketDataFetcher:
    def __init__(self):
        self.coingecko_base = 'https://api.coingecko.com/api/v3'
    
    def get_btc_price(self):
        try:
            url = f"{self.coingecko_base}/simple/price"
            params = {'ids': 'bitcoin', 'vs_currencies': 'usd', 'include_24hr_change': 'true'}
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            return {'price_usd': data['bitcoin']['usd'], 'change_24h': data['bitcoin'].get('usd_24h_change', 0)}
        except:
            return None
    
    def get_trending(self):
        return []
