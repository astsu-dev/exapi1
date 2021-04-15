"""Has binance market data response handler interface."""

from typing import Protocol

from exapi.models.binance import (BinanceAveragePriceModel, BinanceCandles,
                                  BinanceExchangeInfoModel,
                                  BinanceOrderBookModel,
                                  BinanceOrderBookTickerModel,
                                  BinanceOrderBookTickers, BinancePingModel,
                                  BinancePriceTickerModel, BinancePriceTickers,
                                  BinanceServerTimeModel,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTickersPriceChangeStat, BinanceTrades)
from exapi.models.binance.trade import BinanceAggregateTrades
from exapi.requesters.typedefs import RequesterResponse


class IBinanceSpotMarketDataResponseHandler(Protocol):
    """Has methods for handling binance market data responses."""

    async def handle_ping_response(self, res: RequesterResponse) -> BinancePingModel:
        """Handles get ping response.

        Args:
            res (RequesterResponse)

        Returns:
            BinancePingModel
        """

    async def handle_get_server_time_response(self, res: RequesterResponse
                                              ) -> BinanceServerTimeModel:
        """Handles get server time response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceServerTimeModel
        """

    async def handle_get_average_price_response(self, res: RequesterResponse
                                                ) -> BinanceAveragePriceModel:
        """Handles get average price response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceAveragePriceModel
        """

    async def handle_get_candles_response(self, res: RequesterResponse) -> BinanceCandles:
        """Handles get candles response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceCandles
        """

    async def handle_get_exchange_info_response(self, res: RequesterResponse
                                                ) -> BinanceExchangeInfoModel:
        """Handles get exchange info response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceExchangeInfoModel
        """

    async def handle_get_order_book_ticker_response(self, res: RequesterResponse
                                                    ) -> BinanceOrderBookTickerModel:
        """Handles get order book ticker response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderBookTickerModel
        """

    async def handle_get_order_book_tickers_response(self, res: RequesterResponse
                                                     ) -> BinanceOrderBookTickers:
        """Handles get order book tickers response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderBookTickers
        """

    async def handle_get_order_book_response(self, res: RequesterResponse
                                             ) -> BinanceOrderBookModel:
        """Handles get order book response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderBookModel
        """

    async def handle_get_price_ticker_response(self, res: RequesterResponse
                                               ) -> BinancePriceTickerModel:
        """Handles get price ticker response.

        Args:
            res (RequesterResponse)

        Returns:
            BinancePriceTickerModel
        """

    async def handle_get_price_tickers_response(self, res: RequesterResponse
                                                ) -> BinancePriceTickers:
        """Handles get price tickers response.

        Args:
            res (RequesterResponse)

        Returns:
            BinancePriceTickers
        """

    async def handle_get_ticker_price_change_stat_response(self, res: RequesterResponse
                                                           ) -> BinanceTickerPriceChangeStatModel:
        """Handles get ticker price 24hr change statistics response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTickerPriceChangeStatModel
        """

    async def handle_get_tickers_price_change_stat_response(self, res: RequesterResponse
                                                            ) -> BinanceTickersPriceChangeStat:
        """Handles get tickers price 24hr change statistics response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTickersPriceChangeStat
        """

    async def handle_get_trades_response(self, res: RequesterResponse) -> BinanceTrades:
        """Handles get trades response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTrades
        """

    async def handle_get_aggregate_trades_response(self,
                                                   res: RequesterResponse
                                                   ) -> BinanceAggregateTrades:
        """Handles get aggregate trades response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceAggregateTrades
        """
