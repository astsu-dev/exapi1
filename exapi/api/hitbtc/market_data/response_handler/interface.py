"""Has hitbtc market data response handler interface."""

from typing import Protocol

from exapi.api.hitbtc.models import (HitbtcCandles, HitbtcCurrencies,
                                     HitbtcCurrencyModel, HitbtcOrderBookModel,
                                     HitbtcOrderBooks, HitbtcSymbolCandles,
                                     HitbtcSymbolModel, HitbtcSymbols,
                                     HitbtcSymbolTrades, HitbtcTickerModel,
                                     HitbtcTickers, HitbtcTrades)
from exapi.requesters.typedefs import RequesterResponse


class IHitbtcMarketDataResponseHandler(Protocol):
    """Has methods for hanling hitbtc responses."""

    async def handle_get_currencies_response(
            self,
            response: RequesterResponse) -> HitbtcCurrencies:
        """Handles get currencies response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcCurrencies: list of currencies
        """

    async def handle_get_certain_currency_response(
            self,
            response: RequesterResponse) -> HitbtcCurrencyModel:
        """Handles get certain currency response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcCurrencyModel
        """

    async def handle_get_symbols_response(
            self,
            response: RequesterResponse) -> HitbtcSymbols:
        """Handles get symbols response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbols: list of symbols.
        """

    async def handle_get_certain_symbol_response(
            self,
            response: RequesterResponse) -> HitbtcSymbolModel:
        """Handles get certain symbol response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbolModel
        """

    async def handle_get_tickers_response(
            self,
            response: RequesterResponse) -> HitbtcTickers:
        """Handles get tickers response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbols: list of symbols.
        """

    async def handle_get_certain_ticker_response(
            self,
            response: RequesterResponse) -> HitbtcTickerModel:
        """Handles get certain ticker response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcTickerModel
        """

    async def handle_get_trades_response(
            self,
            response: RequesterResponse) -> HitbtcTrades:
        """Handles get trades response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcTrades
        """

    async def handle_get_certain_trades_response(
            self,
            response: RequesterResponse) -> HitbtcSymbolTrades:
        """Handles get certain trades response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbolTrades
        """

    async def handle_get_order_books_response(
            self,
            response: RequesterResponse) -> HitbtcOrderBooks:
        """Handles get trades response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderBooks
        """

    async def handle_get_certain_order_book_response(
            self,
            response: RequesterResponse) -> HitbtcOrderBookModel:
        """Handles get certain order book response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderBookModel
        """

    async def handle_get_candles_response(
            self,
            response: RequesterResponse) -> HitbtcCandles:
        """Handles get candles response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcCandles
        """

    async def handle_get_certain_candles_response(
            self,
            response: RequesterResponse) -> HitbtcSymbolCandles:
        """Handles get certain candles response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbolCandles
        """
