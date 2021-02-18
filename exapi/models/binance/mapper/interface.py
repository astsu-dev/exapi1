"""Has binance models mapper interface."""

from exapi.models.binance import (BinanceAccountInfoJson,
                                  BinanceAccountInfoModel,
                                  BinanceAveragePriceJson,
                                  BinanceAveragePriceModel, BinanceCandleJson,
                                  BinanceCandleModel, BinanceCandles,
                                  BinanceCandlesJson,
                                  BinanceCurrencyBalanceJson,
                                  BinanceCurrencyBalanceModel,
                                  BinanceCurrencyBalances,
                                  BinanceCurrencyBalancesJson,
                                  BinanceExchangeFilterJson,
                                  BinanceExchangeFilterModel,
                                  BinanceExchangeFilters,
                                  BinanceExchangeFiltersJson,
                                  BinanceExchangeInfoJson,
                                  BinanceExchangeInfoModel,
                                  BinanceFilledOrderJson,
                                  BinanceFilledOrderModel, BinanceFilledOrders,
                                  BinanceFilledOrdersJson,
                                  BinanceOrderBookJson, BinanceOrderBookModel,
                                  BinanceOrderBookOrderJson,
                                  BinanceOrderBookOrderModel,
                                  BinanceOrderBookOrders,
                                  BinanceOrderBookOrdersJson,
                                  BinanceOrderBookTickerJson,
                                  BinanceOrderBookTickerModel,
                                  BinanceOrderBookTickers,
                                  BinanceOrderBookTickersJson,
                                  BinanceOrderJson, BinanceOrderModel,
                                  BinanceOrders, BinanceOrdersJson,
                                  BinancePingJson, BinancePingModel,
                                  BinancePriceTickerJson,
                                  BinancePriceTickerModel, BinancePriceTickers,
                                  BinancePriceTickersJson,
                                  BinanceRateLimitJson, BinanceRateLimitModel,
                                  BinanceRateLimits, BinanceRateLimitsJson,
                                  BinanceServerTimeJson,
                                  BinanceServerTimeModel,
                                  BinanceSymbolFilterJson,
                                  BinanceSymbolFilterModel,
                                  BinanceSymbolFilters,
                                  BinanceSymbolFiltersJson, BinanceSymbolJson,
                                  BinanceSymbolModel, BinanceSymbols,
                                  BinanceSymbolsJson,
                                  BinanceTickerPriceChangeStatJson,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTickersPriceChangeStat,
                                  BinanceTickersPriceChangeStatJson,
                                  BinanceTradeJson, BinanceTradeModel,
                                  BinanceTrades, BinanceTradesJson)

from .base import IBinanceBaseModelsMapper


class IBinanceModelsMapper(IBinanceBaseModelsMapper):
    """Binance models mapper interface.

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

    def map_to_candle(self, json: BinanceCandleJson) -> BinanceCandleModel:
        """Maps candle json to candle model.

        Args:
            json (BinanceCandleJson)

        Returns:
            BinanceCandleModel
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

    def map_to_order_book_order(self, json: BinanceOrderBookOrderJson
                                ) -> BinanceOrderBookOrderModel:
        """Maps order book order json to order book order model.

        Args:
            json (BinanceOrderBookOrderJson)

        Returns:
            BinanceOrderBookOrderModel
        """

    def map_to_order_book_orders(self, json: BinanceOrderBookOrdersJson
                                 ) -> BinanceOrderBookOrders:
        """Maps order book orders json to order book orders model.

        Args:
            json (BinanceOrderBookOrdersJson)

        Returns:
            BinanceOrderBookOrders
        """

    def map_to_order_book(self, json: BinanceOrderBookJson) -> BinanceOrderBookModel:
        """Maps order book json to order book model.

        Args:
            json (BinanceOrderBookJson)

        Returns:
            BinanceOrderBookModel
        """

    def map_to_filled_order(self, json: BinanceFilledOrderJson) -> BinanceFilledOrderModel:
        """Maps filled order json to filled order model.

        Args:
            json (BinanceFilledOrderJson)

        Returns:
            BinanceFilledOrderModel
        """

    def map_to_filled_orders(self, json: BinanceFilledOrdersJson) -> BinanceFilledOrders:
        """Maps filled orders json to filled orders model.

        Args:
            json (BinanceFilledOrdersJson)

        Returns:
            BinanceFilledOrders
        """

    def map_to_order(self, json: BinanceOrderJson) -> BinanceOrderModel:
        """Maps order json to order model.

        Args:
            json (BinanceOrderJson)

        Returns:
            BinanceOrderModel
        """

    def map_to_orders(self, json: BinanceOrdersJson) -> BinanceOrders:
        """Maps orders json to orders model.

        Args:
            json (BinanceOrdersJson)

        Returns:
            BinanceOrders
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

    def map_to_trade(self, json: BinanceTradeJson) -> BinanceTradeModel:
        """Maps trade json to trade model.

        Args:
            json (BinanceTradeJson)

        Returns:
            BinanceTradeModel
        """

    def map_to_trades(self, json: BinanceTradesJson) -> BinanceTrades:
        """Maps trades json to trades model.

        Args:
            json (BinanceTradesJson)

        Returns:
            BinanceTrades
        """

    def map_to_symbol_filter(self, json: BinanceSymbolFilterJson) -> BinanceSymbolFilterModel:
        """Maps symbol filter json to symbol filter model.

        Args:
            json (BinanceSymbolFilterJson)

        Returns:
            BinanceSymbolFilterModel
        """

    def map_to_symbol_filters(self, json: BinanceSymbolFiltersJson) -> BinanceSymbolFilters:
        """Maps symbol filters json to symbol filters model.

        Args:
            json (BinanceSymbolFiltersJson)

        Returns:
            BinanceSymbolFilters
        """

    def map_to_symbol(self, json: BinanceSymbolJson) -> BinanceSymbolModel:
        """Maps symbol json to symbol model.

        Args:
            json (BinanceSymbolJson)

        Returns:
            BinanceSymbolModel
        """

    def map_to_symbols(self, json: BinanceSymbolsJson) -> BinanceSymbols:
        """Maps symbols json to symbols model.

        Args:
            json (BinanceSymbolsJson)

        Returns:
            BinanceSymbols
        """

    def map_to_exchange_filter(self, json: BinanceExchangeFilterJson) -> BinanceExchangeFilterModel:
        """Maps exchnage filter json to exchnage filter model.

        Args:
            json (BinanceExchangeFilterJson)

        Returns:
            BinanceExchangeFilterModel
        """

    def map_to_exchange_filters(self, json: BinanceExchangeFiltersJson) -> BinanceExchangeFilters:
        """Maps exchnage filters json to exchnage filters model.

        Args:
            json (BinanceExchangeFilterJson)

        Returns:
            BinanceExchangeFilterModel
        """

    def map_to_rate_limit(self, json: BinanceRateLimitJson) -> BinanceRateLimitModel:
        """Maps rate limit json to rate limit model.

        Args:
            json (BinanceRateLimitJson)

        Returns:
            BinanceRateLimitModel
        """

    def map_to_rate_limits(self, json: BinanceRateLimitsJson) -> BinanceRateLimits:
        """Maps rate limits json to rate limits model.

        Args:
            json (BinanceRateLimitsJson)

        Returns:
            BinanceRateLimits
        """

    def map_to_exchange_info(self, json: BinanceExchangeInfoJson) -> BinanceExchangeInfoModel:
        """Maps exchange info json to exchange info model.

        Args:
            json (BinanceExchangeInfoJson)

        Returns:
            BinanceExchangeInfoModel
        """

    def map_to_balance(self, json: BinanceCurrencyBalanceJson) -> BinanceCurrencyBalanceModel:
        """Maps balance json to balance model.

        Args:
            json (BinanceCurrencyBalanceJson)

        Returns:
            BinanceCurrencyBalanceModel
        """

    def map_to_balances(self, json: BinanceCurrencyBalancesJson) -> BinanceCurrencyBalances:
        """Maps balances json to balances model.

        Args:
            json (BinanceCurrencyBalancesJson)

        Returns:
            BinanceCurrencyBalances
        """

    def map_to_account_info(self, json: BinanceAccountInfoJson) -> BinanceAccountInfoModel:
        """Maps account info json to account info model.

        Args:
            json (BinanceAccountInfoJson)

        Returns:
            BinanceAccountInfoModel
        """
