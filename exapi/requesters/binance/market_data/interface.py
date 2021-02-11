from typing import Optional

from exapi.models.binance.typedefs import CandleInterval
from exapi.requesters.base import IBaseRequester
from exapi.requesters.typedefs import RequesterResponse


class IBinanceMarketDataRequester(IBaseRequester):
    """Has methods for making requests to binance exchange."""

    async def ping(self) -> RequesterResponse:
        """Test connectivity to the Rest API.

        Request weight: 1.

        Json example:
            {}

        Returns:
            RequesterResponse
        """

    async def get_server_time(self) -> RequesterResponse:
        """Test connectivity to the Rest API and get the current server time.

        Request weight: 1.

        Json example:
            {
                "serverTime": 1499827319559
            }

        Returns:
            RequesterResponse
        """

    async def get_exchange_info(self) -> RequesterResponse:
        """Current exchange trading rules and symbol information.

        Request weight: 1.

        Json example:
            {
                "timezone": "UTC",
                "serverTime": 1565246363776,
                "rateLimits": [
                    {
                    // These are defined in the `ENUM definitions`
                    // section under `Rate Limiters (rateLimitType)`.
                    // All limits are optional
                    }
                ],
                "exchangeFilters": [
                    // These are the defined filters in the `Filters` section.
                    // All filters are optional.
                ],
                "symbols": [
                    {
                        "symbol": "ETHBTC",
                        "status": "TRADING",
                        "baseAsset": "ETH",
                        "baseAssetPrecision": 8,
                        "quoteAsset": "BTC",
                        "quotePrecision": 8,
                        "quoteAssetPrecision": 8,
                        "orderTypes": [
                            "LIMIT",
                            "LIMIT_MAKER",
                            "MARKET",
                            "STOP_LOSS",
                            "STOP_LOSS_LIMIT",
                            "TAKE_PROFIT",
                            "TAKE_PROFIT_LIMIT"
                        ],
                        "icebergAllowed": true,
                        "ocoAllowed": true,
                        "isSpotTradingAllowed": true,
                        "isMarginTradingAllowed": true,
                        "filters": [
                            //These are defined in the Filters section.
                            //All filters are optional
                        ],
                        "permissions": [
                            "SPOT",
                            "MARGIN"
                        ]
                    }
                ]
            }

        Returns:
            RequesterResponse
        """

    async def get_order_book(self, symbol: str,
                             limit: Optional[int] = None
                             ) -> RequesterResponse:
        """Gets order book for a certain `symbol`.

        Request weight:
            Adjusted based on the limit:
            | Limit	             | Weight |
            | ------------------ | ------ |
            | 5, 10, 20, 50, 100 | 1      |
            | 500	             | 5      |
            | 1000	             | 10     |
            | 5000	             | 50     |

        Json example:
            {
                "lastUpdateId": 1027024,
                "bids": [
                    [
                        "4.00000000",     // PRICE
                        "431.00000000"    // QTY
                    ]
                ],
                "asks": [
                    [
                        "4.00000200",
                        "12.00000000"
                    ]
                ]
            }

        Args:
            symbol (str): certain symbol.
            limit (Optional[int], optional): Default 100; max 5000.
                Valid limits: [5, 10, 20, 50, 100, 500, 1000, 5000]

        Returns:
            RequesterResponse
        """

    async def get_trades(self, symbol: str,
                         limit: Optional[int] = None
                         ) -> RequesterResponse:
        """Get recent trades for a certain `symbol`.

        Request weight: 1.

        Json example:
            [
                {
                    "id": 28457,
                    "price": "4.00000100",
                    "qty": "12.00000000",
                    "quoteQty": "48.000012",
                    "time": 1499865549590,
                    "isBuyerMaker": true,
                    "isBestMatch": true
                },
                ...
            ]

        Args:
            symbol (str): certain symbol.
            limit (Optional[int], optional): Default 500; max 1000.

        Returns:
            RequesterResponse
        """

    async def get_old_trades(self, symbol: str,
                             limit: Optional[int] = None,
                             from_id: Optional[int] = None
                             ) -> RequesterResponse:
        """Get older market trades for a certain `symbol`.

        Required api key in headers.

        Request weight: 5.

        Json example:
            [
                {
                    "id": 28457,
                    "price": "4.00000100",
                    "qty": "12.00000000",
                    "quoteQty": "48.000012",
                    "time": 1499865549590, // Trade executed timestamp,
                                           // as same as `T` in the stream
                    "isBuyerMaker": true,
                    "isBestMatch": true
                }
            ]

        Args:
            symbol (str): certain symbol.
            from_id (Optional[int]): Trade id to fetch from.
                Default gets most recent trades.
            limit (Optional[int]): Default 500; max 1000.

        Returns:
            RequesterResponse
        """

    async def get_aggregate_trades(self, symbol: str,
                                   from_id: Optional[int] = None,
                                   start_time: Optional[int] = None,
                                   end_time: Optional[int] = None,
                                   limit: Optional[int] = None
                                   ) -> RequesterResponse:
        """Get compressed, aggregate trades for a certain symbol.
        Trades that fill at the time, from the same order,
        with the same price will have the quantity aggregated.

        If start_time and end_time are sent,
        time between start_time and end_time must be less than 1 hour.

        If from_id, start_time, and end_time are not sent,
        the most recent aggregate trades will be returned.

        Request weight: 1.

        Json example:
            [
                {
                    "a": 26129,         // Aggregate tradeId
                    "p": "0.01633102",  // Price
                    "q": "4.70443515",  // Quantity
                    "f": 27781,         // First tradeId
                    "l": 27781,         // Last tradeId
                    "T": 1498793709153, // Timestamp
                    "m": true,          // Was the buyer the maker?
                    "M": true           // Was the trade the best price match?
                }
            ]

        Args:
            symbol (str): certain symbol.
            from_id (Optional[int], optional): id to get aggregate trades from INCLUSIVE.
            start_time (Optional[int], optional): Timestamp in ms to
                get aggregate trades from INCLUSIVE.
            end_time (Optional[int], optional): Timestamp in ms to
                get aggregate trades until INCLUSIVE.
            limit (Optional[int], optional): Default 500; max 1000.

        Returns:
            RequesterResponse
        """

    async def get_candles(self, symbol: str,
                          interval: CandleInterval,
                          start_time: Optional[int] = None,
                          end_time: Optional[int] = None,
                          limit: Optional[int] = None
                          ) -> RequesterResponse:
        """Kline/candlestick bars for a certain `symbol`.
        Klines are uniquely identified by their open time.

        Request weight: 1.

        If start_time and end_time are not sent, the most recent klines are returned.

        Json example:
            [
                [
                    1499040000000,      // Open time
                    "0.01634790",       // Open
                    "0.80000000",       // High
                    "0.01575800",       // Low
                    "0.01577100",       // Close
                    "148976.11427815",  // Volume
                    1499644799999,      // Close time
                    "2434.19055334",    // Quote asset volume
                    308,                // Number of trades
                    "1756.87402397",    // Taker buy base asset volume
                    "28.46694368",      // Taker buy quote asset volume
                    "17928899.62484339" // Ignore.
                ]
            ]

        Args:
            symbol (str): certain symbol.
            interval (CandleInterval)
            start_time (Optional[int], optional)
            end_time (Optional[int], optional)
            limit (Optional[int], optional): Default 500; max 1000.

        Returns:
            RequesterResponse
        """

    async def get_average_price(self, symbol: str) -> RequesterResponse:
        """Current average price for a certain `symbol`.

        Request weight: 1.

        Args:
            symbol (str): certain symbol.

        Returns:
            RequesterResponse
        """

    async def get_ticker_price_change_stat(self, symbol: Optional[str] = None) -> RequesterResponse:
        """24 hour rolling window price change statistics.
        Careful when accessing this with no symbol.

        Request weight: 1 for a single symbol; 
            40 when the symbol parameter is omitted;

        Json example:
            {
                "symbol": "BNBBTC",
                "priceChange": "-94.99999800",
                "priceChangePercent": "-95.960",
                "weightedAvgPrice": "0.29628482",
                "prevClosePrice": "0.10002000",
                "lastPrice": "4.00000200",
                "lastQty": "200.00000000",
                "bidPrice": "4.00000000",
                "askPrice": "4.00000200",
                "openPrice": "99.00000000",
                "highPrice": "100.00000000",
                "lowPrice": "0.10000000",
                "volume": "8913.30000000",
                "quoteVolume": "15.30000000",
                "openTime": 1499783499040,
                "closeTime": 1499869899040,
                "firstId": 28385,   // First tradeId
                "lastId": 28460,    // Last tradeId
                "count": 76         // Trade count
            }
            OR
            [
                {
                    "symbol": "BNBBTC",
                    "priceChange": "-94.99999800",
                    "priceChangePercent": "-95.960",
                    "weightedAvgPrice": "0.29628482",
                    "prevClosePrice": "0.10002000",
                    "lastPrice": "4.00000200",
                    "lastQty": "200.00000000",
                    "bidPrice": "4.00000000",
                    "askPrice": "4.00000200",
                    "openPrice": "99.00000000",
                    "highPrice": "100.00000000",
                    "lowPrice": "0.10000000",
                    "volume": "8913.30000000",
                    "quoteVolume": "15.30000000",
                    "openTime": 1499783499040,
                    "closeTime": 1499869899040,
                    "firstId": 28385,   // First tradeId
                    "lastId": 28460,    // Last tradeId
                    "count": 76         // Trade count
                },
                ...
            ]

        Args:
            symbol (Optional[str], optional): If the symbol is None,
                tickers for all symbols will be returned in an array.

        Returns:
            RequesterResponse
        """

    async def get_price_ticker(self, symbol: Optional[str] = None) -> RequesterResponse:
        """Latest price for a symbol or symbols.

        Request weight: 1 for a single symbol;
            2 when the symbol parameter is omitted

        Json example:
            {
                "symbol": "LTCBTC",
                "price": "4.00000200"
            }
            OR
            [
                {
                    "symbol": "LTCBTC",
                    "price": "4.00000200"
                },
                ...
            ]

        Args:
            symbol (Optional[str], optional): If the symbol is not sent,
                prices for all symbols will be returned in an array.

        Returns:
            RequesterResponse
        """

    async def get_order_book_ticker(self, symbol: Optional[str] = None) -> RequesterResponse:
        """Best price/qty on the order book for a `symbol` or all symbols.

        Request weight: 1 for a single symbol;
            2 when the symbol parameter is omitted

        Json example:
            {
                "symbol": "LTCBTC",
                "bidPrice": "4.00000000",
                "bidQty": "431.00000000",
                "askPrice": "4.00000200",
                "askQty": "9.00000000"
            }
            OR
            [
                {
                    "symbol": "LTCBTC",
                    "bidPrice": "4.00000000",
                    "bidQty": "431.00000000",
                    "askPrice": "4.00000200",
                    "askQty": "9.00000000"
                },
                ...
            ]

        Args:
            symbol (Optional[str], optional): If the symbol is not sent,
                bookTickers for all symbols will be returned in an array.


        Returns:
            RequesterResponse
        """
