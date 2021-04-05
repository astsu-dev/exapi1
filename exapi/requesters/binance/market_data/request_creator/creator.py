"""Has binance market data request creator."""

from typing import Optional

from exapi.typedefs.binance import CandleInterval
from exapi.requesters.binance.auth import IBinanceKeyAuth
from exapi.requesters.binance.base.request_creator import \
    BinanceBaseRequestCreator
from exapi.requesters.request import Request
from exapi.requesters.typedefs import Params
from yarl import URL

from .interface import IBinanceMarketDataRequestCreator


class BinanceMarketDataRequestCreator(BinanceBaseRequestCreator, IBinanceMarketDataRequestCreator):
    """Has methods for creating requests for binance market data endpoints."""

    def __init__(self, auth: IBinanceKeyAuth) -> None:
        """Class initialization.

        Args:
            auth (IBinanceKeyAuth): auth which adds api key to request headers.
        """

        self._auth = auth

    def create_ping_request(self) -> Request:
        """Creates ping request.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/ping"))
        req = Request(method=method, url=url)

        return req

    def create_get_server_time_request(self) -> Request:
        """Creates get server time request.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/time"))
        req = Request(method=method, url=url)

        return req

    def create_get_exchange_info_request(self) -> Request:
        """Creates get exchange information request.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/exchangeInfo"))
        req = Request(method=method, url=url)

        return req

    def create_get_order_book_request(self, symbol: str,
                                      limit: Optional[int] = None
                                      ) -> Request:
        """Creates get order book request.

        Args:
            symbol (str): certain symbol.
            limit (Optional[int], optional): Default 100; max 5000.
                Valid limits: [5, 10, 20, 50, 100, 500, 1000, 5000]

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/depth"))
        params: Params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = str(limit)
        url = url.with_query(params)

        req = Request(method=method, url=url)

        return req

    def create_get_trades_request(self, symbol: str,
                                  limit: Optional[int] = None
                                  ) -> Request:
        """Creates get trades request.

        Args:
            symbol (str): certain symbol.
            limit (Optional[int], optional): Default 500; max 1000.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/trades"))
        params: Params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = str(limit)
        url = url.with_query(params)

        req = Request(method=method, url=url)

        return req

    def create_get_old_trades_request(self, symbol: str,
                                      limit: Optional[int] = None,
                                      from_id: Optional[int] = None
                                      ) -> Request:
        """Creates get old trades request.

        Args:
            symbol (str): certain symbol.
            from_id (Optional[int]): Trade id to fetch from.
                Default gets most recent trades.
            limit (Optional[int]): Default 500; max 1000.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/historicalTrades"))
        params: Params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = str(limit)
        if from_id is not None:
            params["fromId"] = str(from_id)
        url = url.with_query(params)

        headers = self._auth.sign()

        req = Request(method=method, url=url, headers=headers)

        return req

    def create_get_aggregate_trades_request(self, symbol: str,
                                            from_id: Optional[int] = None,
                                            start_time: Optional[int] = None,
                                            end_time: Optional[int] = None,
                                            limit: Optional[int] = None
                                            ) -> Request:
        """Creates get aggregate trades request.

        Args:
            symbol (str): certain symbol.
            from_id (Optional[int], optional): id to get aggregate trades from INCLUSIVE.
            start_time (Optional[int], optional): Timestamp in ms to
                get aggregate trades from INCLUSIVE.
            end_time (Optional[int], optional): Timestamp in ms to
                get aggregate trades until INCLUSIVE.
            limit (Optional[int], optional): Default 500; max 1000.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/aggTrades"))
        params: Params = {
            "symbol": symbol
        }
        if from_id is not None:
            params["fromId"] = str(from_id)
        if start_time is not None:
            params["startTime"] = str(start_time)
        if end_time is not None:
            params["endTime"] = str(end_time)
        if limit is not None:
            params["limit"] = str(limit)
        url = url.with_query(params)

        req = Request(method=method, url=url)

        return req

    def create_get_candles_request(self, symbol: str,
                                   interval: CandleInterval,
                                   start_time: Optional[int] = None,
                                   end_time: Optional[int] = None,
                                   limit: Optional[int] = None
                                   ) -> Request:
        """Creates get candles request.

        Args:
            symbol (str): certain symbol.
            interval (CandleInterval)
            start_time (Optional[int], optional)
            end_time (Optional[int], optional)
            limit (Optional[int], optional): Default 500; max 1000.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/klines"))
        params: Params = {
            "symbol": symbol,
            "interval": interval
        }
        if start_time is not None:
            params["startTime"] = str(start_time)
        if end_time is not None:
            params["endTime"] = str(end_time)
        if limit is not None:
            params["limit"] = str(limit)
        url = url.with_query(params)

        req = Request(method=method, url=url)

        return req

    def create_get_average_price_request(self, symbol: str) -> Request:
        """Creates get average price request.

        Args:
            symbol (str): certain symbol.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/avgPrice"))
        params: Params = {
            "symbol": symbol
        }
        url = url.with_query(params)

        req = Request(method=method, url=url)

        return req

    def create_get_ticker_price_change_stat_request(self, symbol: Optional[str] = None) -> Request:
        """Creates get 24 hr ticker price change statistics request.

        Args:
            symbol (Optional[str], optional): If the symbol is None,
                tickers for all symbols will be returned in an array.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/ticker/24hr"))
        params: Params = {}
        if symbol is not None:
            params["symbol"] = symbol
        url = url.with_query(params)

        req = Request(method=method, url=url)

        return req

    def create_get_price_ticker_request(self, symbol: Optional[str] = None) -> Request:
        """Creates get price ticker request.

        Args:
            symbol (Optional[str], optional): If the symbol is not sent,
                prices for all symbols will be returned in an array.

        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/ticker/price"))
        params: Params = {}
        if symbol is not None:
            params["symbol"] = symbol
        url = url.with_query(params)

        req = Request(method=method, url=url)

        return req

    def create_get_order_book_ticker_request(self, symbol: Optional[str] = None) -> Request:
        """Creates get order book ticker request.

        Args:
            symbol (Optional[str], optional): If the symbol is not sent,
                bookTickers for all symbols will be returned in an array.


        Returns:
            Request
        """

        method = "GET"
        url = URL(self._create_url("/ticker/bookTicker"))
        params: Params = {}
        if symbol is not None:
            params["symbol"] = symbol
        url = url.with_query(params)

        req = Request(method=method, url=url)

        return req
