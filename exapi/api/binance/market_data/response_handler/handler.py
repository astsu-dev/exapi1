"""Has binance market data response handler."""

from typing import Optional

from exapi.api.binance.base import BinanceBaseResponseHandler
from exapi.api.binance.market_data.response_handler.interface import IBinanceMarketDataResponseHandler
from exapi.models.binance import (BinanceAggregateTrades,
                                  BinanceAggregateTradesJson,
                                  BinanceAveragePriceJson,
                                  BinanceAveragePriceModel, BinanceCandles,
                                  BinanceCandlesJson, BinanceExchangeInfoJson,
                                  BinanceExchangeInfoModel,
                                  BinanceOrderBookJson, BinanceOrderBookModel,
                                  BinanceOrderBookTickerJson,
                                  BinanceOrderBookTickerModel,
                                  BinanceOrderBookTickers,
                                  BinanceOrderBookTickersJson, BinancePingJson,
                                  BinancePingModel, BinancePriceTickerJson,
                                  BinancePriceTickerModel, BinancePriceTickers,
                                  BinancePriceTickersJson,
                                  BinanceServerTimeJson,
                                  BinanceServerTimeModel,
                                  BinanceTickerPriceChangeStatJson,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTickersPriceChangeStat,
                                  BinanceTickersPriceChangeStatJson,
                                  BinanceTrades, BinanceTradesJson)
from exapi.models.binance.mapper import BinanceModelsMapper
from exapi.models.binance.mapper.market_data import \
    IBinanceMarketDataModelsMapper
from exapi.requesters.typedefs import RequesterResponse


class BinanceMarketDataResponseHandler(BinanceBaseResponseHandler, IBinanceMarketDataResponseHandler):
    """Has methods for handling binance market data responses."""

    _models_mapper: IBinanceMarketDataModelsMapper

    def __init__(self, models_mapper: Optional[IBinanceMarketDataModelsMapper] = None,
                 json_content_type: Optional[str] = "application/json"
                 ) -> None:
        models_mapper = models_mapper if models_mapper is not None else BinanceModelsMapper()
        super().__init__(models_mapper, json_content_type)

    async def handle_ping_response(self, res: RequesterResponse) -> BinancePingModel:
        """Handles get ping response.

        Args:
            res (RequesterResponse)

        Returns:
            BinancePingModel
        """

        json_res: BinancePingJson = await self.handle_response(res)
        return self._models_mapper.map_to_ping(json_res)

    async def handle_get_server_time_response(self, res: RequesterResponse
                                              ) -> BinanceServerTimeModel:
        """Handles get server time response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceServerTimeModel
        """

        json_res: BinanceServerTimeJson = await self.handle_response(res)
        return self._models_mapper.map_to_server_time(json_res)

    async def handle_get_average_price_response(self, res: RequesterResponse
                                                ) -> BinanceAveragePriceModel:
        """Handles get average price response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceAveragePriceModel
        """

        json_res: BinanceAveragePriceJson = await self.handle_response(res)
        return self._models_mapper.map_to_average_price(json_res)

    async def handle_get_candles_response(self, res: RequesterResponse) -> BinanceCandles:
        """Handles get candles response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceCandles
        """

        json_res: BinanceCandlesJson = await self.handle_response(res)
        return self._models_mapper.map_to_candles(json_res)

    async def handle_get_exchange_info_response(self, res: RequesterResponse
                                                ) -> BinanceExchangeInfoModel:
        """Handles get exchange info response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceExchangeInfoModel
        """

        json_res: BinanceExchangeInfoJson = await self.handle_response(res)
        return self._models_mapper.map_to_exchange_info(json_res)

    async def handle_get_order_book_ticker_response(self, res: RequesterResponse
                                                    ) -> BinanceOrderBookTickerModel:
        """Handles get order book ticker response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderBookTickerModel
        """

        json_res: BinanceOrderBookTickerJson = await self.handle_response(res)
        return self._models_mapper.map_to_order_book_ticker(json_res)

    async def handle_get_order_book_tickers_response(self, res: RequesterResponse
                                                     ) -> BinanceOrderBookTickers:
        """Handles get order book tickers response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderBookTickers
        """

        json_res: BinanceOrderBookTickersJson = await self.handle_response(res)
        return self._models_mapper.map_to_order_book_tickers(json_res)

    async def handle_get_order_book_response(self, res: RequesterResponse
                                             ) -> BinanceOrderBookModel:
        """Handles get order book response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderBookModel
        """

        json_res: BinanceOrderBookJson = await self.handle_response(res)
        return self._models_mapper.map_to_order_book(json_res)

    async def handle_get_price_ticker_response(self, res: RequesterResponse
                                               ) -> BinancePriceTickerModel:
        """Handles get price ticker response.

        Args:
            res (RequesterResponse)

        Returns:
            BinancePriceTickerModel
        """

        json_res: BinancePriceTickerJson = await self.handle_response(res)
        return self._models_mapper.map_to_price_ticker(json_res)

    async def handle_get_price_tickers_response(self, res: RequesterResponse
                                                ) -> BinancePriceTickers:
        """Handles get price tickers response.

        Args:
            res (RequesterResponse)

        Returns:
            BinancePriceTickers
        """

        json_res: BinancePriceTickersJson = await self.handle_response(res)
        return self._models_mapper.map_to_price_tickers(json_res)

    async def handle_get_ticker_price_change_stat_response(self, res: RequesterResponse
                                                           ) -> BinanceTickerPriceChangeStatModel:
        """Handles get ticker price 24hr change statistics response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTickerPriceChangeStatModel
        """

        json_res: BinanceTickerPriceChangeStatJson = await self.handle_response(res)
        return self._models_mapper.map_to_ticker_price_change_stat(json_res)

    async def handle_get_tickers_price_change_stat_response(self, res: RequesterResponse
                                                            ) -> BinanceTickersPriceChangeStat:
        """Handles get tickers price 24hr change statistics response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTickersPriceChangeStat
        """

        json_res: BinanceTickersPriceChangeStatJson = await self.handle_response(res)
        return self._models_mapper.map_to_tickers_price_change_stat(json_res)

    async def handle_get_trades_response(self, res: RequesterResponse) -> BinanceTrades:
        """Handles get trades response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTrades
        """

        json_res: BinanceTradesJson = await self.handle_response(res)
        return self._models_mapper.map_to_trades(json_res)

    async def handle_get_aggregate_trades_response(self,
                                                   res: RequesterResponse
                                                   ) -> BinanceAggregateTrades:
        """Handles get aggregate trades response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceAggregateTrades
        """

        json_res: BinanceAggregateTradesJson = await self.handle_response(res)
        return self._models_mapper.map_to_aggregate_trades(json_res)
