"""Has binance market data models mapper interface."""

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
from exapi.models.binance.mapper.base import IBinanceBaseModelsMapper
from exapi.models.binance.trade import BinanceAggregateTradeModel


class IBinanceMarketDataModelsMapper(IBinanceBaseModelsMapper):
    """Binance market data models mapper interface.

    Maps json to models.
    """

    def map_to_ping(self, json: BinancePingJson) -> BinancePingModel:
        """Maps ping json to ping model.

        Args:
            json (BinancePingJson)

        Returns:
            BinancePingModel
        """

    def map_to_server_time(self, json: BinanceServerTimeJson) -> BinanceServerTimeModel:
        """Maps server time json to server time model.

        Args:
            json (BinanceServerTimeJson)

        Returns:
            BinanceServerTimeModel
        """

    def map_to_average_price(self, json: BinanceAveragePriceJson) -> BinanceAveragePriceModel:
        """Maps average price json to average price model.

        Args:
            json (BinanceAveragePriceJson)

        Returns:
            BinanceAveragePriceModel
        """

    def map_to_candles(self, json: BinanceCandlesJson) -> BinanceCandles:
        """Maps candles json to candles model.

        Args:
            json (BinanceCandlesJson)

        Returns:
            BinanceCandles
        """

    def map_to_order_book_ticker(self, json: BinanceOrderBookTickerJson
                                 ) -> BinanceOrderBookTickerModel:
        """Maps order book ticker json to order book ticker model.

        Args:
            json (BinanceOrderBookTickerJson)

        Returns:
            BinanceOrderBookTickerModel
        """

    def map_to_order_book_tickers(self, json: BinanceOrderBookTickersJson
                                  ) -> BinanceOrderBookTickers:
        """Maps order book tickers json to order book tickers model.

        Args:
            json (BinanceOrderBookTickersJson)

        Returns:
            BinanceOrderBookTickersModel
        """

    def map_to_order_book(self, json: BinanceOrderBookJson) -> BinanceOrderBookModel:
        """Maps order book json to order book model.

        Args:
            json (BinanceOrderBookJson)

        Returns:
            BinanceOrderBookModel
        """

    def map_to_price_ticker(self, json: BinancePriceTickerJson) -> BinancePriceTickerModel:
        """Maps price ticker json to price ticker model.

        Args:
            json (BinancePriceTickerJson)

        Returns:
            BinancePriceTickerModel
        """

    def map_to_price_tickers(self, json: BinancePriceTickersJson) -> BinancePriceTickers:
        """Maps price tickers json to price tickers model.

        Args:
            json (BinancePriceTickersJson)

        Returns:
            BinancePriceTickers
        """

    def map_to_ticker_price_change_stat(self, json: BinanceTickerPriceChangeStatJson
                                        ) -> BinanceTickerPriceChangeStatModel:
        """Maps ticker price change statistics json
        to ticker price change statistics model.

        Args:
            json (BinanceTickerPriceChangeStatJson)

        Returns:
            BinanceTickerPriceChangeStatModel
        """

    def map_to_tickers_price_change_stat(self, json: BinanceTickersPriceChangeStatJson
                                         ) -> BinanceTickersPriceChangeStat:
        """Maps tickers price change statistics json
        to tickers price change statistics model.

        Args:
            json (BinanceTickersPriceChangeStatJson)

        Returns:
            BinanceTickersPriceChangeStat
        """

    def map_to_trades(self, json: BinanceTradesJson) -> BinanceTrades:
        """Maps trades json to trades model.

        Args:
            json (BinanceTradesJson)

        Returns:
            BinanceTrades
        """

    def map_to_aggregate_trades(self, json: BinanceAggregateTradesJson) -> BinanceAggregateTrades:
        """Maps aggregate trades json to aggregate trades model.

        Args:
            json (BinanceAggregateTradesJson)

        Returns:
            BinanceAggregateTrades
        """

    def map_to_exchange_info(self, json: BinanceExchangeInfoJson) -> BinanceExchangeInfoModel:
        """Maps exchange info json to exchange info model.

        Args:
            json (BinanceExchangeInfoJson)

        Returns:
            BinanceExchangeInfoModel
        """
