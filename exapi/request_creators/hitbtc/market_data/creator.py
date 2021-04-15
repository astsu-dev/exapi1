"""Has interface for hitbtc market data request creator."""

from typing import Optional

from yarl import URL

from exapi.request_creators.hitbtc.base import HitbtcBaseRequestCreator
from exapi.request_creators.request import Request
from exapi.requesters.typedefs import Params
from exapi.typedefs.hitbtc import (CandlesPeriod, Currencies, Currency,
                                   IntervalValue, SortBy, SortDirection,
                                   Symbol, Symbols)


class HitbtcMarketDataRequestCreator(HitbtcBaseRequestCreator):
    """Has methods for creating requests for hitbtc market data endpoints."""

    BASE_URL: str = HitbtcBaseRequestCreator.BASE_URL + "/api/2/public"

    def create_get_currencies_request(self, currencies: Optional[Currencies] = None) -> Request:
        """Creates request for /public/currency endpoint.

        Requires no API key Access Rights.

        Args:
            currencies (Optional[Currencies], optional): specified currencies.
                If not passed, then will create for all currencies.

        Returns:
            Request
        """

        path = "/currency"
        url = URL(self._create_url(path))
        params: Params = {}
        if currencies is not None:
            params["currencies"] = ",".join(currencies)
        url = url.with_query(params)

        return Request(method="GET", url=url)

    def create_get_certain_currency_request(self, currency: Currency) -> Request:
        """Creates request for /public/currency/`currency` endpoint.

        Requires no API key Access Rights.

        Args:
            currency (Currency)

        Returns:
            Request
        """

        path = f"/currency/{currency}"
        url = URL(self._create_url(path))

        return Request(method="GET", url=url)

    def create_get_symbols_request(self, symbols: Optional[Symbols] = None) -> Request:
        """Creates request for /public/symbol endpoint.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will create for all symbols.

        Returns:
            Request
        """

        path = "/symbol"
        url = URL(self._create_url(path))
        params: Params = {}
        if symbols is not None:
            params["symbols"] = ",".join(symbols)
        url = url.with_query(params)

        return Request(method="GET", url=url)

    def create_get_certain_symbol_request(self, symbol: Symbol) -> Request:
        """Creates request for /public/symbol/`symbol` endpoint.

        Requires no API key Access Rights.

        Args:
            symbol (Symbol): certain symbol

        Returns:
            Request
        """

        path = f"/symbol/{symbol}"
        url = URL(self._create_url(path))

        return Request(method="GET", url=url)

    def create_get_tickers_request(self, symbols: Optional[Symbols] = None) -> Request:
        """Creates request for /public/ticker endpoint.

        Requires no API key Access Rights.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will create for all symbols.

        Returns:
            Request
        """

        path = "/ticker"
        url = URL(self._create_url(path))
        params: Params = {}
        if symbols is not None:
            params["symbols"] = ",".join(symbols)
        url = url.with_query(params)

        return Request(method="GET", url=url)

    def create_get_certain_ticker_request(self, symbol: Symbol) -> Request:
        """Creates request for /public/ticker/`symbol` endpoint.

        Requires no API key Access Rights.

        Args:
            symbol (Symbol): certain symbol

        Returns:
            Request
        """

        path = f"/ticker/{symbol}"
        url = URL(self._create_url(path))

        return Request(method="GET", url=url)

    def create_get_trades_request(self, symbols: Optional[Symbols] = None,
                                  sort: Optional[SortDirection] = None,
                                  from_: Optional[IntervalValue] = None,
                                  till: Optional[IntervalValue] = None,
                                  limit: Optional[int] = None,
                                  offset: Optional[int] = None
                                  ) -> Request:
        """Creates request for /public/trades endpoint.

        Requires no API key Access Rights.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will create for all symbols.
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
            Request
        """

        path = "/trades"
        url = URL(self._create_url(path))
        params: Params = {}
        if symbols is not None:
            params["symbols"] = ",".join(symbols)
        if sort is not None:
            params["sort"] = sort
        if from_ is not None:
            params["from"] = str(from_)
        if till is not None:
            params["till"] = str(till)
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        url = url.with_query(params)

        return Request(method="GET", url=url)

    def create_get_certain_trades_request(self, symbol: Symbol,
                                          sort: Optional[SortDirection] = None,
                                          by: Optional[SortBy] = None,
                                          from_: Optional[IntervalValue] = None,
                                          till: Optional[IntervalValue] = None,
                                          limit: Optional[int] = None,
                                          offset: Optional[int] = None
                                          ) -> Request:
        """Creates request for /public/trades/`symbol` endpoint.

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
            Request
        """

        path = f"/trades/{symbol}"
        url = URL(self._create_url(path))
        params: Params = {}
        if sort is not None:
            params["sort"] = sort
        if by is not None:
            params["by"] = by
        if from_ is not None:
            params["from"] = str(from_)
        if till is not None:
            params["till"] = str(till)
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        url = url.with_query(params)

        return Request(method="GET", url=url)

    def create_get_orderbooks_request(self, symbols: Optional[Symbols] = None,
                                      limit: Optional[int] = None
                                      ) -> Request:
        """Creates request for /public/orderbook endpoint.

        Requires no API key Access Rights.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will create for all symbols.
            limit (Optional[int], optional): limit of order book levels.
                Default value: 100. Set 0 to view full list of levels.

        Returns:
            Request
        """

        path = "/orderbook"
        url = URL(self._create_url(path))
        params: Params = {}
        if symbols is not None:
            params["symbols"] = ",".join(symbols)
        if limit is not None:
            params["limit"] = str(limit)
        url = url.with_query(params)

        return Request(method="GET", url=url)

    def create_get_certain_orderbook_request(self, symbol: Symbol,
                                             limit: Optional[int] = None,
                                             volume: Optional[int] = None
                                             ) -> Request:
        """Creates request for /public/orderbook/`symbol` endpoint.

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
            Request
        """

        path = f"/orderbook/{symbol}"
        url = URL(self._create_url(path))
        params: Params = {}
        if limit is not None:
            params["limit"] = str(limit)
        if volume is not None:
            params["volume"] = str(volume)
        url = url.with_query(params)

        return Request(method="GET", url=url)

    def create_get_candles_request(self, symbols: Optional[Symbols] = None,
                                   period: Optional[CandlesPeriod] = None,
                                   sort: Optional[SortDirection] = None,
                                   from_: Optional[IntervalValue] = None,
                                   till: Optional[IntervalValue] = None,
                                   limit: Optional[int] = None,
                                   offset: Optional[int] = None
                                   ) -> Request:
        """Creates request for /public/candles endpoint.

        Requires no API key Access Rights.

        Args:
            symbols (Optional[Symbols], optional): list of symbols.
                If not passed, then will create for all symbols.
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
            Request
        """

        path = "/candles"
        url = URL(self._create_url(path))
        params: Params = {}
        if symbols is not None:
            params["symbols"] = ",".join(symbols)
        if period is not None:
            params["period"] = period
        if sort is not None:
            params["sort"] = sort
        if from_ is not None:
            params["from"] = str(from_)
        if till is not None:
            params["till"] = str(till)
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        url = url.with_query(params)

        return Request(method="GET", url=url)

    def create_get_certain_candles_request(self, symbol: Symbol,
                                           period: Optional[CandlesPeriod] = None,
                                           sort: Optional[SortDirection] = None,
                                           from_: Optional[IntervalValue] = None,
                                           till: Optional[IntervalValue] = None,
                                           limit: Optional[int] = None,
                                           offset: Optional[int] = None
                                           ) -> Request:
        """Creates request for /public/candles/`symbol` endpoint.

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
            Request
        """

        path = f"/candles/{symbol}"
        url = URL(self._create_url(path))
        params: Params = {}
        if period is not None:
            params["period"] = period
        if sort is not None:
            params["sort"] = sort
        if from_ is not None:
            params["from"] = str(from_)
        if till is not None:
            params["till"] = str(till)
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        url = url.with_query(params)

        return Request(method="GET", url=url)

    def _create_url(self, path: str) -> str:
        return self.BASE_URL + path
