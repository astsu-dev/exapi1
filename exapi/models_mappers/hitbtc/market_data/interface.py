"""Has hitbtc market data models mapper interface."""

from exapi.models.hitbtc import (HitbtcCandleModel, HitbtcCandles, HitbtcCurrencies, HitbtcCurrencyModel,
                                 HitbtcOrderBookModel, HitbtcOrderBookOrderModel, HitbtcOrderBooks,
                                 HitbtcRawCandleModel, HitbtcRawCandles, HitbtcRawCurrencies, HitbtcRawCurrencyModel,
                                 HitbtcRawOrderBookModel, HitbtcRawOrderBookOrderModel, HitbtcRawOrderBooks,
                                 HitbtcRawSymbolCandles, HitbtcRawSymbolModel, HitbtcRawSymbolTrades, HitbtcRawSymbols,
                                 HitbtcRawTickerModel, HitbtcRawTickers, HitbtcRawTradeModel, HitbtcRawTrades,
                                 HitbtcSymbolCandles, HitbtcSymbolModel, HitbtcSymbolTrades, HitbtcSymbols,
                                 HitbtcTickerModel, HitbtcTickers, HitbtcTradeModel, HitbtcTrades)
from exapi.models_mappers.hitbtc.base import IHitbtcBaseModelsMapper


class IHitbtcMarketDataModelsMapper(IHitbtcBaseModelsMapper):
    """Has methods for mapping hitbtc market data json models
    to hitbtc dataclass models.
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
