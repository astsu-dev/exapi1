"""Has hitbtc market data response handler interface."""

from typing import Optional

from exapi.api.hitbtc.base import HitbtcBaseResponseHandler
from exapi.models_mappers.hitbtc.market_data import \
    IHitbtcMarketDataModelsMapper
from exapi.api.hitbtc.market_data.response_handler.interface import IHitbtcMarketDataResponseHandler
from exapi.models.hitbtc import (HitbtcCandles, HitbtcCurrencies, HitbtcCurrencyModel, HitbtcOrderBookModel,
                                 HitbtcOrderBooks, HitbtcRawCandles, HitbtcRawCurrencies, HitbtcRawCurrencyModel,
                                 HitbtcRawOrderBookModel, HitbtcRawOrderBooks, HitbtcRawSymbolCandles,
                                 HitbtcRawSymbolModel, HitbtcRawSymbolTrades, HitbtcRawSymbols, HitbtcRawTickerModel,
                                 HitbtcRawTickers, HitbtcRawTrades, HitbtcSymbolCandles, HitbtcSymbolModel,
                                 HitbtcSymbolTrades, HitbtcSymbols, HitbtcTickerModel, HitbtcTickers, HitbtcTrades)
from exapi.models_mappers.hitbtc import HitbtcModelsMapper
from exapi.requesters.typedefs import RequesterResponse


class HitbtcMarketDataResponseHandler(HitbtcBaseResponseHandler, IHitbtcMarketDataResponseHandler):
    """Has methods for hanling hitbtc responses."""

    _models_mapper: IHitbtcMarketDataModelsMapper

    def __init__(self, models_mapper: Optional[IHitbtcMarketDataModelsMapper] = None,
                 json_content_type: Optional[str] = "application/json"
                 ) -> None:
        models_mapper = (
            models_mapper if models_mapper is not None else HitbtcModelsMapper())
        super().__init__(models_mapper, json_content_type)

    async def handle_get_currencies_response(
            self,
            response: RequesterResponse) -> HitbtcCurrencies:
        """Handles get currencies response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcCurrencies: list of currencies
        """

        raw_currencies: HitbtcRawCurrencies = await self.handle_response(response)
        res = self._models_mapper.map_to_currencies(raw_currencies)
        return res

    async def handle_get_certain_currency_response(
            self,
            response: RequesterResponse) -> HitbtcCurrencyModel:
        """Handles get certain currency response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcCurrencyModel
        """

        raw: HitbtcRawCurrencyModel = await self.handle_response(response)
        res = self._models_mapper.map_to_currency(raw)
        return res

    async def handle_get_symbols_response(
            self,
            response: RequesterResponse) -> HitbtcSymbols:
        """Handles get symbols response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbols: list of symbols.
        """

        raw: HitbtcRawSymbols = await self.handle_response(response)
        res = self._models_mapper.map_to_symbols(raw)
        return res

    async def handle_get_certain_symbol_response(
            self,
            response: RequesterResponse) -> HitbtcSymbolModel:
        """Handles get certain symbol response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbolModel
        """

        raw: HitbtcRawSymbolModel = await self.handle_response(response)
        res = self._models_mapper.map_to_symbol(raw)
        return res

    async def handle_get_tickers_response(
            self,
            response: RequesterResponse) -> HitbtcTickers:
        """Handles get tickers response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbols: list of symbols.
        """

        raw: HitbtcRawTickers = await self.handle_response(response)
        res = self._models_mapper.map_to_tickers(raw)
        return res

    async def handle_get_certain_ticker_response(
            self,
            response: RequesterResponse) -> HitbtcTickerModel:
        """Handles get certain ticker response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcTickerModel
        """

        raw: HitbtcRawTickerModel = await self.handle_response(response)
        res = self._models_mapper.map_to_ticker(raw)
        return res

    async def handle_get_trades_response(
            self,
            response: RequesterResponse) -> HitbtcTrades:
        """Handles get trades response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcTrades
        """

        raw: HitbtcRawTrades = await self.handle_response(response)
        res = self._models_mapper.map_to_trades(raw)
        return res

    async def handle_get_certain_trades_response(
            self,
            response: RequesterResponse) -> HitbtcSymbolTrades:
        """Handles get certain trades response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbolTrades
        """

        raw: HitbtcRawSymbolTrades = await self.handle_response(response)
        res = self._models_mapper.map_to_symbol_trades(raw)
        return res

    async def handle_get_order_books_response(
            self,
            response: RequesterResponse) -> HitbtcOrderBooks:
        """Handles get trades response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderBooks
        """

        raw: HitbtcRawOrderBooks = await self.handle_response(response)
        res = self._models_mapper.map_to_orderbooks(raw)
        return res

    async def handle_get_certain_order_book_response(
            self,
            response: RequesterResponse) -> HitbtcOrderBookModel:
        """Handles get certain order book response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderBookModel
        """

        raw: HitbtcRawOrderBookModel = await self.handle_response(response)
        res = self._models_mapper.map_to_orderbook(raw)
        return res

    async def handle_get_candles_response(
            self,
            response: RequesterResponse) -> HitbtcCandles:
        """Handles get candles response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcCandles
        """

        raw: HitbtcRawCandles = await self.handle_response(response)
        res = self._models_mapper.map_to_candles(raw)
        return res

    async def handle_get_certain_candles_response(
            self,
            response: RequesterResponse) -> HitbtcSymbolCandles:
        """Handles get certain candles response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcSymbolCandles
        """

        raw: HitbtcRawSymbolCandles = await self.handle_response(response)
        res = self._models_mapper.map_to_symbol_candles(raw)
        return res
