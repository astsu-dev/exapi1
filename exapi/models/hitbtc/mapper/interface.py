"""Has hitbtc models mapper interface."""

from typing import Union

from exapi.models.hitbtc import (HitbtcCandleModel, HitbtcCandles, HitbtcCurrencies, HitbtcCurrencyModel,
                                 HitbtcErrorModel, HitbtcOrderBookModel, HitbtcOrderBookOrderModel, HitbtcOrderBooks,
                                 HitbtcOrderModel, HitbtcOrders, HitbtcRawCandleModel, HitbtcRawCandles,
                                 HitbtcRawCurrencies, HitbtcRawCurrencyModel, HitbtcRawDetailedErrorModel,
                                 HitbtcRawErrorModel, HitbtcRawOrderBookModel, HitbtcRawOrderBookOrderModel,
                                 HitbtcRawOrderBooks, HitbtcRawOrderModel, HitbtcRawOrders, HitbtcRawSymbolCandles,
                                 HitbtcRawSymbolModel, HitbtcRawSymbolTrades, HitbtcRawSymbols, HitbtcRawTickerModel,
                                 HitbtcRawTickers, HitbtcRawTradeModel, HitbtcRawTrades,
                                 HitbtcRawTradingCurrencyBalanceModel, HitbtcRawTradingCurrencyBalances,
                                 HitbtcRawTradingFeeModel, HitbtcSymbolCandles, HitbtcSymbolModel, HitbtcSymbolTrades,
                                 HitbtcSymbols, HitbtcTickerModel, HitbtcTickers, HitbtcTradeModel, HitbtcTrades,
                                 HitbtcTradingCurrencyBalanceModel, HitbtcTradingCurrencyBalances,
                                 HitbtcTradingFeeModel)
from exapi.models.hitbtc.mapper.base import IHitbtcBaseModelsMapper


class IHitbtcModelsMapper(IHitbtcBaseModelsMapper):
    """Has methods for mapping hitbtc json models
    to hitbtc dataclass models.
    """

    def map_to_error(self, raw_error: Union[HitbtcRawErrorModel,
                                            HitbtcRawDetailedErrorModel]
                     ) -> HitbtcErrorModel:
        """Maps error json model to error dataclass model.

        Args:
            raw_error (Union[HitbtcRawErrorModel, HitbtcRawDetailedErrorModel])

        Returns:
            HitbtcErrorModel
        """

    def map_to_currency(self, raw_currency: HitbtcRawCurrencyModel) -> HitbtcCurrencyModel:
        """Maps currency json to currency model.

        Args:
            raw_currency (HitbtcRawCurrency)

        Returns:
            HitbtcCurrencyModel
        """

    def map_to_currencies(self, raw_currencies: HitbtcRawCurrencies) -> HitbtcCurrencies:
        """Maps currencies json to currencies model.

        Args:
            raw_currencies (HitbtcRawCurrencies)

        Returns:
            HitbtcCurrencies
        """

    def map_to_symbol(self, raw_symbol: HitbtcRawSymbolModel) -> HitbtcSymbolModel:
        """Maps symbol json to symbol model.

        Args:
            raw_symbol (HitbtcRawSymbol)

        Returns:
            HitbtcSymbolModel
        """

    def map_to_symbols(self, raw_symbols: HitbtcRawSymbols) -> HitbtcSymbols:
        """Maps symbols json to symbols model.

        Args:
            raw_symbols (HitbtcRawSymbols)

        Returns:
            HitbtcSymbols
        """

    def map_to_orderbook_order(self, raw_orderbook_order: HitbtcRawOrderBookOrderModel
                               ) -> HitbtcOrderBookOrderModel:
        """Maps orderbook order json to orderbook order model.

        Args:
            raw_orderbook_order (HitbtcRawOrderBookOrder)

        Returns:
            HitbtcOrderBookOrder
        """

    def map_to_orderbook(self, raw_orderbook: HitbtcRawOrderBookModel
                         ) -> HitbtcOrderBookModel:
        """Maps orderbook json to orderbook model.

        Args:
            raw_orderbook (HitbtcRawOrderBookModel)

        Returns:
            HitbtcOrderBookModel
        """

    def map_to_orderbooks(self, raw_orderbooks: HitbtcRawOrderBooks) -> HitbtcOrderBooks:
        """Maps orderbooks json to orderbooks model.

        Args:
            raw_orderbook (HitbtcRawOrderBooks)

        Returns:
            HitbtcOrderBooks
        """

    def map_to_ticker(self, raw_ticker: HitbtcRawTickerModel) -> HitbtcTickerModel:
        """Maps ticker json to ticker model.

        Args:
            raw_ticker (HitbtcRawTicker)

        Returns:
            HitbtcTickerModel
        """

    def map_to_tickers(self, raw_tickers: HitbtcRawTickers) -> HitbtcTickers:
        """Maps tickers json to tickers model.

        Args:
            raw_ticker (HitbtcRawTickers)

        Returns:
            HitbtcTickers
        """

    def map_to_trade(self, raw_trade: HitbtcRawTradeModel) -> HitbtcTradeModel:
        """Maps trade json to trade model.

        Args:
            raw_trades (HitbtcRawTradeModel)

        Returns:
            HitbtcTradeModel
        """

    def map_to_trades(self, raw_trades: HitbtcRawTrades) -> HitbtcTrades:
        """Maps trades json to trades.

        Args:
            raw_trades (HitbtcRawTrades)

        Returns:
            HitbtcTrades
        """

    def map_to_symbol_trades(self, raw_trades: HitbtcRawSymbolTrades) -> HitbtcSymbolTrades:
        """Maps symbol trades json to symbol trades model.

        Args:
            raw_trades (HitbtcRawTrade)

        Returns:
            HitbtcSymbolTrades
        """

    def map_to_candle(self, raw_candle: HitbtcRawCandleModel) -> HitbtcCandleModel:
        """Maps candle json to candle.

        Args:
            raw_candle (HitbtcRawCandle)

        Returns:
            HitbtcCandleModel
        """

    def map_to_candles(self, raw_candles: HitbtcRawCandles) -> HitbtcCandles:
        """Maps candles json to candles.

        Args:
            raw_candles (HitbtcRawCandles)

        Returns:
            HitbtcCandles
        """

    def map_to_symbol_candles(self, raw_candles: HitbtcRawSymbolCandles) -> HitbtcSymbolCandles:
        """Maps symbol candles json to symbol candles model.

        Args:
            raw_candles (HitbtcRawTrade)

        Returns:
            HitbtcSymbolCandles
        """

    def map_to_order(self, raw_order: HitbtcRawOrderModel) -> HitbtcOrderModel:
        """Maps order json to order model.

        Args:
            raw_order (HitbtcRawOrderModel)

        Returns:
            HitbtcOrderModel
        """

    def map_to_orders(self, raw_orders: HitbtcRawOrders) -> HitbtcOrders:
        """Maps orders json to list of order.

        Args:
            raw_orders (HitbtcRawOrders)

        Returns:
            HitbtcOrders
        """

    def map_to_trading_currency_balance(self, raw_balance: HitbtcRawTradingCurrencyBalanceModel
                                        ) -> HitbtcTradingCurrencyBalanceModel:
        """Maps trading currency balance json to trading currency balance.

        Args:
            raw_balance (HitbtcRawTradingCurrencyBalanceModel)

        Returns:
            HitbtcTradingCurrencyBalanceModel
        """

    def map_to_trading_balance(self, raw_balance: HitbtcRawTradingCurrencyBalances
                               ) -> HitbtcTradingCurrencyBalances:
        """Maps trading balance json to trading balance.

        Args:
            raw_balance (HitbtcRawTradingCurrencyBalances)

        Returns:
            HitbtcTradingCurrencyBalances
        """

    def map_to_trading_fee(self, raw_fee: HitbtcRawTradingFeeModel) -> HitbtcTradingFeeModel:
        """Maps orders json to list of order.

        Args:
            raw_orders (HitbtcRawOrders)

        Returns:
            HitbtcOrders
        """
