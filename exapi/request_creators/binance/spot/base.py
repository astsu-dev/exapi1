from exapi.request_creators.base import BaseRequestCreator


class BinanceBaseSpotRequestCreator(BaseRequestCreator):
    """Binance base spot request creator."""

    BASE_URL: str = "https://api.binance.com"
