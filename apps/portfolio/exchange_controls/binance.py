from binance.client import Client
from apps.portfolio.models.exchange import BINANCE
from apps.portfolio.models import Exchange


class BinanceExchange(object):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(api_key, api_secret)

