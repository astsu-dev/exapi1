from typing import Optional, Protocol

from exapi.typedefs.binance import CandleInterval
from exapi.requesters.request import Request


class IBinanceMarketDataRequestCreator(Protocol):
    """Has methods for creating requests for binance market data endpoints."""

    def create_ping_request(self) -> Request:
        """Creates ping request.

        Returns:
            Request
        """

    def create_get_server_time_request(self) -> Request:
        """Creates get server time request.

        Returns:
            Request
        """

    def create_get_exchange_info_request(self) -> Request:
        """Creates get exchange information request.

        Returns:
            Request
        """

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

    def create_get_average_price_request(self, symbol: str) -> Request:
        """Creates get average price request.

        Args:
            symbol (str): certain symbol.

        Returns:
            Request
        """

    def create_get_ticker_price_change_stat_request(self, symbol: Optional[str] = None) -> Request:
        """Creates get 24 hr ticker price change statistics request.

        Args:
            symbol (Optional[str], optional): If the symbol is None,
                tickers for all symbols will be returned in an array.

        Returns:
            Request
        """

    def create_get_price_ticker_request(self, symbol: Optional[str] = None) -> Request:
        """Creates get price ticker request.

        Args:
            symbol (Optional[str], optional): If the symbol is not sent,
                prices for all symbols will be returned in an array.

        Returns:
            Request
        """

    def create_get_order_book_ticker_request(self, symbol: Optional[str] = None) -> Request:
        """Creates get order book ticker request.

        Args:
            symbol (Optional[str], optional): If the symbol is not sent,
                bookTickers for all symbols will be returned in an array.


        Returns:
            Request
        """
