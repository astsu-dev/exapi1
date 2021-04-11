"""Has hitbtc market data api."""

from typing import Optional

from exapi.models.hitbtc import (HitbtcCandles, HitbtcCurrencies,
                                 HitbtcCurrencyModel, HitbtcOrderBookModel,
                                 HitbtcOrderBooks, HitbtcSymbolCandles,
                                 HitbtcSymbolModel, HitbtcSymbols,
                                 HitbtcSymbolTrades, HitbtcTickerModel,
                                 HitbtcTickers, HitbtcTrades)
from exapi.requesters.hitbtc.market_data import IHitbtcMarketDataRequester
from exapi.typedefs.hitbtc import (CandlesPeriod, Currencies, Currency,
                                   IntervalValue, SortBy, SortDirection,
                                   Symbol, Symbols)

from exapi.api.hitbtc.market_data.interface import IHitbtcMarketDataAPI
from exapi.api.hitbtc.market_data.response_handler import (HitbtcMarketDataResponseHandler,
                               IHitbtcMarketDataResponseHandler)


class HitbtcMarketDataAPI(IHitbtcMarketDataAPI):
    """Has methods for market data requests making."""

    def __init__(self, requester: IHitbtcMarketDataRequester,
                 response_handler: Optional[IHitbtcMarketDataResponseHandler] = None
                 ) -> None:
        self._requester = requester
        self._handler = (response_handler if response_handler is not None else
                         HitbtcMarketDataResponseHandler())

    async def get_currencies(self, currencies: Optional[Currencies] = None) -> HitbtcCurrencies:
        """Gets a list of all currencies or specified currencies.

        Returns the actual list of available currencies, tokens, etc.

        Requires no API key Access Rights.

        Args:
            currencies (Optional[Currencies], optional): specified currencies.
                If not passed, then will return all currencies.

        Returns:
            HitbtcCurrencies
        """

        response = await self._requester.get_currencies(currencies)
        res = await self._handler.handle_get_currencies_response(response)
        return res

    async def get_certain_currency(self, currency: Currency) -> HitbtcCurrencyModel:
        """Gets a certain currency.

        Returns the data for a certain currency.

        Requires no API key Access Rights.

        Args:
            currency (Currency)

        Returns:
            HitbtCurrencyModel
        """

        response = await self._requester.get_certain_currency(currency)
        res = await self._handler.handle_get_certain_currency_response(response)
        return res

    async def get_symbols(self, symbols: Optional[Symbols] = None) -> HitbtcSymbols:
        """Gets a list of all symbols or specified symbols.

        Returns the actual list of currency symbols (currency pairs)
        traded on exchange. The first listed currency of a symbol
        is called the base currency, and the second currency is called the quote currency.
        The currency pair indicates how much of the quote currency is needed
        to purchase one unit of the base currency.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will return all symbols.

        Returns:
            HitbtcSymbols
        """

        response = await self._requester.get_symbols(symbols)
        res = await self._handler.handle_get_symbols_response(response)
        return res

    async def get_certain_symbol(self, symbol: Symbol) -> HitbtcSymbolModel:
        """Gets a certain symbol.

        Returns the data for a certain symbol.

        Requires no API key Access Rights.

        Args:
            symbol (Symbol): certain symbol

        Returns:
            HitbtcSymbolModel
        """

        response = await self._requester.get_certain_symbol(symbol)
        res = await self._handler.handle_get_certain_symbol_response(response)
        return res

    async def get_tickers(self, symbols: Optional[Symbols] = None) -> HitbtcTickers:
        """Gets tickers for all symbols or for specified symbols.

        Returns tickers information.

        Requires no API key Access Rights.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will return for all symbols.

        Returns:
            RequesterResponse: aiohttp response
        """

        response = await self._requester.get_tickers(symbols)
        res = await self._handler.handle_get_tickers_response(response)
        return res

    async def get_certain_ticker(self, symbol: Symbol) -> HitbtcTickerModel:
        """Gets ticker for a certain symbol.

        Returns the ticker for a certain symbol.

        Requires no API key Access Rights.

        Args:
            symbol (Symbol): certain symbol

        Returns:
            RequesterResponse: aiohttp response
        """

        response = await self._requester.get_certain_ticker(symbol)
        res = await self._handler.handle_get_certain_ticker_response(response)
        return res

    async def get_trades(self, symbols: Optional[Symbols] = None,
                         sort: Optional[SortDirection] = None,
                         from_: Optional[IntervalValue] = None,
                         till: Optional[IntervalValue] = None,
                         limit: Optional[int] = None,
                         offset: Optional[int] = None
                         ) -> HitbtcTrades:
        """Gets trades for all symbols or for specified symbols.

        Returns response with trades information for a symbol with a symbol Id.

        Requires no API key Access Rights.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will return for all symbols.
            SortDirection (Optional[SortDirection], optional): SortDirection direction.
                Accepted values: ASC, DESC. Default value: DESC.
            from_ (Optional[IntervalValue], optional): Interval initial value.
                If sorting by timestamp is used, then Datetime,
                otherwise int of index value.
            till (Optional[IntervalValue], optional): Interval end value.
                If sorting by timestamp is used, then Datetime,
                otherwise int of index value.
            limit (Optional[int], optional): Default value: 100. Max value: 1000.
            offset (Optional[int], optional): Default value: 0. Max value: 100000.

        Returns:
            HitbtcTrades
        """

        response = await self._requester.get_trades(
            symbols=symbols,
            sort=sort,
            from_=from_,
            till=till,
            limit=limit,
            offset=offset)
        res = await self._handler.handle_get_trades_response(response)
        return res

    async def get_certain_trades(self, symbol: Symbol,
                                 sort: Optional[SortDirection] = None,
                                 by: Optional[SortBy] = None,
                                 from_: Optional[IntervalValue] = None,
                                 till: Optional[IntervalValue] = None,
                                 limit: Optional[int] = None,
                                 offset: Optional[int] = None
                                 ) -> HitbtcSymbolTrades:
        """Gets trades for a certain symbol.

        Returns response with trades information for a symbol with a symbol Id.

        Requires no API key Access Rights.

        Args:
            symbol (Symbol): certain symbol.
            sort (Optional[SortDirection], optional): SortDirection direction.
                Accepted values: ASC, DESC. Default value: DESC.
            by (Optional[SortBy], optional): Defines sort type.
                Accepted values: id, timestamp. Default value: timestamp.
            from_ (Optional[IntervalValue], optional): Interval initial value.
                If sorting by timestamp is used, then Datetime,
                otherwise int of index value.
            till (Optional[IntervalValue], optional): Interval end value.
                If sorting by timestamp is used, then Datetime,
                otherwise int of index value.
            limit (Optional[int], optional): Default value: 100. Max value: 1000.
            offset (Optional[int], optional): Default value: 0. Max value: 100000.

        Returns:
            HitbtcSymbolTrades
        """

        response = await self._requester.get_certain_trades(
            symbol=symbol,
            sort=sort,
            by=by,
            from_=from_,
            till=till,
            limit=limit,
            offset=offset)
        res = await self._handler.handle_get_certain_trades_response(response)
        return res

    async def get_orderbooks(self, symbols: Optional[Symbols] = None,
                             limit: Optional[int] = None
                             ) -> HitbtcOrderBooks:
        """Gets order book for all symbols or for specified symbols.

        An order book is an electronic list of buy and sell orders
        for a specific symbol, structured by price level.

        Requires no API key Access Rights.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will return for all symbols.
            limit (Optional[int], optional): limit of order book levels.
                Default value: 100. Set 0 to view full list of levels.

        Returns:
            HitbtcOrderBooks
        """

        response = await self._requester.get_orderbooks(
            symbols=symbols,
            limit=limit)
        res = await self._handler.handle_get_order_books_response(response)
        return res

    async def get_certain_orderbook(self, symbol: Symbol,
                                    limit: Optional[int] = None,
                                    volume: Optional[int] = None
                                    ) -> HitbtcOrderBookModel:
        """Gets order book for a certain symbol.

        Returns an order book for a certain symbol.

        Requires no API key Access Rights.

        Please note that if the volume is specified,
        the limit will be ignored, askAveragePrice and bidAveragePrice
        are returned in response.

        Args:
            symbol (Symbol): certain symbol.
            limit (Optional[int], optional): Limit of Order Book levels.
                Default value: 100. Set 0 to view full list of levels.
            volume (Optional[int], optional): Desired volume for market depth search.

        Returns:
            HitbtcOrderBookModel
        """

        response = await self._requester.get_certain_orderbook(
            symbol=symbol,
            limit=limit,
            volume=volume)
        res = await self._handler.handle_get_certain_order_book_response(response)
        return res

    async def get_candles(self, symbols: Optional[Symbols] = None,
                          period: Optional[CandlesPeriod] = None,
                          sort: Optional[SortDirection] = None,
                          from_: Optional[IntervalValue] = None,
                          till: Optional[IntervalValue] = None,
                          limit: Optional[int] = None,
                          offset: Optional[int] = None
                          ) -> HitbtcCandles:
        """Gets candles for all symbols or for specified symbols.

        Candles are used for the representation of a specific symbol as an OHLC chart.

        Requires no API key Access Rights.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will return for all symbols.
            period (Optional[CandlesPeriod], optional): accepted values: M1 (one minute),
                M3, M5, M15, M30, H1 (one hour), H4,
                D1 (one day), D7, 1M (one month).
                Default value: M30
            sort (Optional[SortDirection], optional): sort direction.
                Accepted values: ASC, DESC. Default value: DESC.
            from_ (Optional[IntervalValue], optional): interval initial value.
            till (Optional[IntervalValue], optional): interval end value.
            limit (Optional[int], optional): limit of candles. Default value: 100. Max value: 1000.
            offset (Optional[int], optional): Default value: 0. Max value: 100000.

        Returns:
            HitbtcCandles
        """

        response = await self._requester.get_candles(
            symbols=symbols,
            period=period,
            sort=sort,
            from_=from_,
            till=till,
            limit=limit,
            offset=offset)
        res = await self._handler.handle_get_candles_response(response)
        return res

    async def get_certain_candles(self, symbol: Symbol,
                                  period: Optional[CandlesPeriod] = None,
                                  sort: Optional[SortDirection] = None,
                                  from_: Optional[IntervalValue] = None,
                                  till: Optional[IntervalValue] = None,
                                  limit: Optional[int] = None,
                                  offset: Optional[int] = None
                                  ) -> HitbtcSymbolCandles:
        """Gets candles for a certain symbol.

        Returns candles for a certain symbol.

        Requires no API key Access Rights.

        Args:
            symbol (Symbol): certain symbol.
            period (Optional[CandlesPeriod], optional): accepted values: M1 (one minute),
                M3, M5, M15, M30, H1 (one hour), H4,
                D1 (one day), D7, 1M (one month).
                Default value: M30
            sort (Optional[SortDirection], optional): sort direction.
                Accepted values: ASC, DESC. Default value: DESC.
            from_ (Optional[IntervalValue], optional): interval initial value.
            till (Optional[IntervalValue], optional): interval end value.
            limit (Optional[int], optional): limit of candles. Default value: 100. Max value: 1000.
            offset (Optional[int], optional): Default value: 0. Max value: 100000.

        Returns:
            HitbtcSymbolCandles
        """

        response = await self._requester.get_certain_candles(
            symbol=symbol,
            period=period,
            sort=sort,
            from_=from_,
            till=till,
            limit=limit,
            offset=offset)
        res = await self._handler.handle_get_certain_candles_response(response)
        return res
