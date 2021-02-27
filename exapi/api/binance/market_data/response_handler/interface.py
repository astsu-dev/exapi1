"""Has binance market data response handler interface."""

from typing import Protocol

from exapi.models.binance import (BinanceAveragePriceModel, BinanceCandles,
                                  BinanceExchangeInfoModel,
                                  BinanceOrderBookModel,
                                  BinanceOrderBookTickerModel,
                                  BinanceOrderBookTickers, BinanceOrderModel,
                                  BinanceOrders, BinancePingModel,
                                  BinancePriceTickerJson,
                                  BinancePriceTickerModel, BinancePriceTickers,
                                  BinanceServerTimeModel,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTickersPriceChangeStat, BinanceTrades)
from exapi.requesters.typedefs import RequesterResponse


class IBinanceMarketDataResponseHandler(Protocol):
    """Has methods for handling binance market data responses."""

    def handle_get_ping_response(self, res: RequesterResponse) -> BinancePingModel:
        """Handles get ping response.

        Args:
            res (RequesterResponse)

        Returns:
            BinancePingModel
        """

    def handle_get_server_time_response(self, res: RequesterResponse
                                        ) -> BinanceServerTimeModel:
        """Handles get server time response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceServerTimeModel
        """

    def handle_get_average_price_response(self, res: RequesterResponse
                                          ) -> BinanceAveragePriceModel:
        """Handles get average price response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceAveragePriceModel
        """

    def handle_get_candles_response(self, res: RequesterResponse) -> BinanceCandles:
        """Handles get candles response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceCandles
        """

    def handle_get_exchange_info_response(self, res: RequesterResponse
                                          ) -> BinanceExchangeInfoModel:
        """Handles get exchange info response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceExchangeInfoModel
        """

    def handle_get_order_book_ticker_response(self, res: RequesterResponse
                                              ) -> BinanceOrderBookTickerModel:
        """Handles get order book ticker response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderBookTickerModel
        """

    def handle_get_order_book_tickers_response(self, res: RequesterResponse
                                               ) -> BinanceOrderBookTickers:
        """Handles get order book tickers response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderBookTickers
        """

    def handle_get_order_book_response(self, res: RequesterResponse
                                       ) -> BinanceOrderBookModel:
        """Handles get order book response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderBookModel
        """

    def handle_get_order_response(self, res: RequesterResponse) -> BinanceOrderModel:
        """Handles get order response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderModel
        """

    def handle_get_orders_response(self, res: RequesterResponse) -> BinanceOrders:
        """Handles get orders response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrders
        """

    def handle_get_price_ticker_response(self, json: BinancePriceTickerJson
                                         ) -> BinancePriceTickerModel:
        """Handles get price ticker response.

        Args:
            res (RequesterResponse)

        Returns:
            BinancePriceTickerModel
        """

    def handle_get_price_tickers_response(self, res: RequesterResponse
                                          ) -> BinancePriceTickers:
        """Handles get price tickers response.

        Args:
            res (RequesterResponse)

        Returns:
            BinancePriceTickers
        """

    def handle_get_ticker_price_change_stat_response(self, res: RequesterResponse
                                                     ) -> BinanceTickerPriceChangeStatModel:
        """Handles get ticker price 24hr change statistics response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTickerPriceChangeStatModel
        """

    def handle_get_tickers_price_change_stat_response(self, res: RequesterResponse
                                                      ) -> BinanceTickersPriceChangeStat:
        """Handles get tickers price 24hr change statistics response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTickersPriceChangeStat
        """

    def handle_get_trades_response(self, res: RequesterResponse) -> BinanceTrades:
        """Handles get trades response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTrades
        """
