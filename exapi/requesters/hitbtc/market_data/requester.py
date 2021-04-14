"""Has hitbtc market data requester."""

from typing import Optional

from exapi.request_creators.hitbtc.market_data import HitbtcMarketDataRequestCreator, IHitbtcMarketDataRequestCreator
from exapi.requesters.base import BaseRequester
from exapi.requesters.hitbtc.market_data.interface import IHitbtcMarketDataRequester
from exapi.requesters.typedefs import RequesterResponse, Session
from exapi.typedefs.hitbtc import (CandlesPeriod, Currencies, Currency,
                                   IntervalValue, SortBy, SortDirection,
                                   Symbol, Symbols)


class HitbtcMarketDataRequester(BaseRequester, IHitbtcMarketDataRequester):
    """Has methods for market data requests making."""

    def __init__(self, session: Session,
                 creator: Optional[IHitbtcMarketDataRequestCreator] = None
                 ) -> None:
        """Class initialization.

        Args:
            session (Optional[aiohttp.ClientSession], optional): aiohttp session. Defaults to None.
            creator (Optional[IHitbtcMarketDataRequestCreator], optional): request creator.
                Defaults to None.
        """

        super().__init__(session)
        self._creator = creator if creator is not None else HitbtcMarketDataRequestCreator()

    async def get_currencies(self, currencies: Optional[Currencies] = None) -> RequesterResponse:
        """Gets a list of all currencies or specified currencies.

        Returns response with response with the actual list of available currencies, tokens, etc.

        Requires no API key Access Rights.

        Args:
            currencies (Optional[Currencies], optional): specified currencies.
                If not passed, then will return all currencies.

        Returns:
            RequesterResponse: aiohttp response
        """

        req = self._creator.create_get_currencies_request(currencies)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_certain_currency(self, currency: Currency) -> RequesterResponse:
        """Gets a certain currency.

        Returns response with the data for a certain currency.

        Requires no API key Access Rights.

        Args:
            currency (Currency)

        Returns:
            RequesterResponse: aiohttp response
        """

        req = self._creator.create_get_certain_currency_request(currency)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_symbols(self, symbols: Optional[Symbols] = None) -> RequesterResponse:
        """Gets a list of all symbols or specified symbols.

        Returns response with the actual list of currency symbols (currency pairs)
        traded on exchange. The first listed currency of a symbol
        is called the base currency, and the second currency is called the quote currency.
        The currency pair indicates how much of the quote currency is needed
        to purchase one unit of the base currency.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will return all symbols.

        Returns:
            RequesterResponse: aiohttp response
        """

        req = self._creator.create_get_symbols_request(symbols)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_certain_symbol(self, symbol: Symbol) -> RequesterResponse:
        """Gets a certain symbol.

        Returns response with the data for a certain symbol.

        Requires no API key Access Rights.

        Args:
            symbol (Symbol): certain symbol

        Returns:
            RequesterResponse: aiothtp response
        """

        req = self._creator.create_get_certain_symbol_request(symbol)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_tickers(self, symbols: Optional[Symbols] = None) -> RequesterResponse:
        """Gets tickers for all symbols or for specified symbols.

        Returns response with ticker information.

        Requires no API key Access Rights.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will return for all symbols.

        Returns:
            RequesterResponse: aiohttp response
        """

        req = self._creator.create_get_tickers_request(symbols)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_certain_ticker(self, symbol: Symbol) -> RequesterResponse:
        """Gets ticker for a certain symbol.

        Returns response with the ticker for a certain symbol.

        Requires no API key Access Rights.

        Args:
            symbol (Symbol): certain symbol

        Returns:
            RequesterResponse: aiohttp response
        """

        req = self._creator.create_get_certain_ticker_request(symbol)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_trades(self, symbols: Optional[Symbols] = None,
                         sort: Optional[SortDirection] = None,
                         from_: Optional[IntervalValue] = None,
                         till: Optional[IntervalValue] = None,
                         limit: Optional[int] = None,
                         offset: Optional[int] = None
                         ) -> RequesterResponse:
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
            RequesterResponse: aiohttp response.
        """

        req = self._creator.create_get_trades_request(
            symbols=symbols,
            sort=sort,
            from_=from_,
            till=till,
            limit=limit,
            offset=offset)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_certain_trades(self, symbol: Symbol,
                                 sort: Optional[SortDirection] = None,
                                 by: Optional[SortBy] = None,
                                 from_: Optional[IntervalValue] = None,
                                 till: Optional[IntervalValue] = None,
                                 limit: Optional[int] = None,
                                 offset: Optional[int] = None
                                 ) -> RequesterResponse:
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
            RequesterResponse: aiohttp response.
        """

        req = self._creator.create_get_certain_trades_request(
            symbol=symbol,
            sort=sort,
            from_=from_,
            till=till,
            limit=limit,
            offset=offset)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_orderbooks(self, symbols: Optional[Symbols] = None,
                             limit: Optional[int] = None
                             ) -> RequesterResponse:
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
            RequesterResponse: aiohttp response.
        """

        req = self._creator.create_get_orderbooks_request(
            symbols=symbols, limit=limit)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_certain_orderbook(self, symbol: Symbol,
                                    limit: Optional[int] = None,
                                    volume: Optional[int] = None
                                    ) -> RequesterResponse:
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
            RequesterResponse: aiohttp response.
        """

        req = self._creator.create_get_certain_orderbook_request(
            symbol=symbol, limit=limit, volume=volume)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_candles(self, symbols: Optional[Symbols] = None,
                          period: Optional[CandlesPeriod] = None,
                          sort: Optional[SortDirection] = None,
                          from_: Optional[IntervalValue] = None,
                          till: Optional[IntervalValue] = None,
                          limit: Optional[int] = None,
                          offset: Optional[int] = None
                          ) -> RequesterResponse:
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
            RequesterResponse: aiohttp response.
        """

        req = self._creator.create_get_candles_request(
            symbols=symbols,
            period=period,
            sort=sort,
            from_=from_,
            till=till,
            limit=limit,
            offset=offset)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)

    async def get_certain_candles(self, symbol: Symbol,
                                  period: Optional[CandlesPeriod] = None,
                                  sort: Optional[SortDirection] = None,
                                  from_: Optional[IntervalValue] = None,
                                  till: Optional[IntervalValue] = None,
                                  limit: Optional[int] = None,
                                  offset: Optional[int] = None
                                  ) -> RequesterResponse:
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
            RequesterResponse: aiohttp response.
        """

        req = self._creator.create_get_certain_candles_request(
            symbol=symbol,
            period=period,
            sort=sort,
            from_=from_,
            till=till,
            limit=limit,
            offset=offset)

        return await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)
