from decimal import Decimal
from typing import Final
from unittest import mock

import pytest
from exapi.api.binance.market_data.response_handler import \
    BinanceMarketDataResponseHandler
from exapi.models.binance import (BinanceAveragePriceModel, BinanceCandleModel,
                                  BinanceExchangeInfoModel,
                                  BinanceLotSizeSymbolFilterModel,
                                  BinanceMaxNumAlgoOrdersExchangeFilterModel,
                                  BinanceMaxNumOrdersExchangeFilterModel,
                                  BinanceOrderBookModel,
                                  BinanceOrderBookOrderModel,
                                  BinanceOrderBookOrdersJson,
                                  BinanceOrderBookTickerModel,
                                  BinanceOrdersRateLimitModel,
                                  BinancePercentPriceSymbolFilterModel,
                                  BinancePingModel, BinancePriceTickerModel,
                                  BinanceRawRequestsRateLimitModel,
                                  BinanceRequestWeightRateLimitModel,
                                  BinanceServerTimeModel, BinanceSymbolModel,
                                  BinanceSymbolsJson,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTradeJson, BinanceTradeModel)
from exapi.models.binance.mapper import BinanceModelsMapper
from exapi.models.binance.mapper.market_data.interface import \
    IBinanceMarketDataModelsMapper

HANDLE_RESPONSE_PATH: Final[str] = "exapi.api.binance.market_data.response_handler.handler.BinanceMarketDataResponseHandler.handle_response"


@pytest.fixture(scope="module")
def handler() -> BinanceMarketDataResponseHandler:
    mapper: IBinanceMarketDataModelsMapper = BinanceModelsMapper()
    return BinanceMarketDataResponseHandler(mapper)


@pytest.mark.asyncio
async def test_handle_ping_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = BinancePingModel()
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {}
        assert await handler.handle_ping_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_server_time_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = BinanceServerTimeModel(server_time=1500)
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "serverTime": 1500
        }
        assert await handler.handle_get_server_time_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_average_price_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = BinanceAveragePriceModel(mins=10, price=Decimal("1500.2"))
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "mins": 10,
            "price": "1500.2"
        }
        assert await handler.handle_get_average_price_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_candles_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = [
        BinanceCandleModel(
            open_time=1500,
            open=Decimal("1500.5"),
            high=Decimal("1500.6"),
            low=Decimal("1500.7"),
            close=Decimal("1500.8"),
            volume=Decimal("1500.9"),
            close_time=1600,
            quote_volume=Decimal("1500.0"),
            trades_num=150,
            taker_buy_base_volume=Decimal("1500.4"),
            taker_buy_quote_volume=Decimal("1500.3"),
            ignore=Decimal("1500.2")),
        BinanceCandleModel(
            open_time=1505,
            open=Decimal("1500.5"),
            high=Decimal("1500.6"),
            low=Decimal("1500.7"),
            close=Decimal("1500.8"),
            volume=Decimal("1500.9"),
            close_time=1600,
            quote_volume=Decimal("1500.0"),
            trades_num=150,
            taker_buy_base_volume=Decimal("1500.4"),
            taker_buy_quote_volume=Decimal("1500.3"),
            ignore=Decimal("1500.2"))
    ]
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
            (
                1500,
                "1500.5",
                "1500.6",
                "1500.7",
                "1500.8",
                "1500.9",
                1600,
                "1500.0",
                150,
                "1500.4",
                "1500.3",
                "1500.2"
            ),
            (
                1505,
                "1500.5",
                "1500.6",
                "1500.7",
                "1500.8",
                "1500.9",
                1600,
                "1500.0",
                150,
                "1500.4",
                "1500.3",
                "1500.2"
            )
        ]
        assert await handler.handle_get_candles_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_exchange_info_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = BinanceExchangeInfoModel(
        timezone="UTC",
        server_time=500,
        rate_limits=[
            BinanceRequestWeightRateLimitModel(
                rate_limit_type="REQUEST_WEIGHT",
                interval="SECOND",
                interval_num=10,
                limit=20),
            BinanceOrdersRateLimitModel(
                rate_limit_type="ORDERS",
                interval="SECOND",
                interval_num=10,
                limit=20),
            BinanceRawRequestsRateLimitModel(
                rate_limit_type="RAW_REQUESTS",
                interval="SECOND",
                interval_num=10,
                limit=20)
        ],
        exchange_filters=[
            BinanceMaxNumOrdersExchangeFilterModel(
                filter_type="EXCHANGE_MAX_NUM_ORDERS",
                max_num_orders=10),
            BinanceMaxNumAlgoOrdersExchangeFilterModel(
                filter_type="EXCHANGE_MAX_ALGO_ORDERS",
                max_num_algo_orders=10)
        ],
        symbols=[
            BinanceSymbolModel(
                symbol="BTCUSDT",
                status="TRADING",
                base_asset="BTC",
                base_asset_precision=8,
                quote_asset="USDT",
                quote_precision=2,
                quote_asset_precision=4,
                order_types=["LIMIT", "STOP_LOSS"],
                iceberg_allowed=False,
                oco_allowed=False,
                is_spot_trading_allowed=True,
                is_margin_trading_allowed=True,
                filters=[
                    BinancePercentPriceSymbolFilterModel(
                        filter_type="PERCENT_PRICE",
                        multiplier_down=Decimal("10.3"),
                        multiplier_up=Decimal("10.4"),
                        avg_price_mins=10),
                    BinanceLotSizeSymbolFilterModel(
                        filter_type="LOT_SIZE",
                        min_qty=Decimal("10.1"),
                        max_qty=Decimal("10.4"),
                        step_size=Decimal("1.2"))
                ],
                permissions=["SPOT", "MARGIN"]),
            BinanceSymbolModel(
                symbol="BTCUSDT",
                status="TRADING",
                base_asset="BTC",
                base_asset_precision=8,
                quote_asset="USDT",
                quote_precision=2,
                quote_asset_precision=4,
                order_types=["LIMIT", "STOP_LOSS"],
                iceberg_allowed=False,
                oco_allowed=False,
                is_spot_trading_allowed=True,
                is_margin_trading_allowed=True,
                filters=[
                    BinancePercentPriceSymbolFilterModel(
                        filter_type="PERCENT_PRICE",
                        multiplier_down=Decimal("10.3"),
                        multiplier_up=Decimal("10.4"),
                        avg_price_mins=10),
                    BinanceLotSizeSymbolFilterModel(
                        filter_type="LOT_SIZE",
                        min_qty=Decimal("10.1"),
                        max_qty=Decimal("10.4"),
                        step_size=Decimal("1.2"))
                ],
                permissions=["SPOT", "MARGIN"])
        ])
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "timezone": "UTC",
            "serverTime": 500,
            "rateLimits": [
                {
                    "rateLimitType": "REQUEST_WEIGHT",
                    "interval": "SECOND",
                    "intervalNum": 10,
                    "limit": 20
                },
                {
                    "rateLimitType": "ORDERS",
                    "interval": "SECOND",
                    "intervalNum": 10,
                    "limit": 20
                },
                {
                    "rateLimitType": "RAW_REQUESTS",
                    "interval": "SECOND",
                    "intervalNum": 10,
                    "limit": 20
                }
            ],
            "exchangeFilters": [
                {
                    "filterType": "EXCHANGE_MAX_NUM_ORDERS",
                    "maxNumOrders": 10
                },
                {
                    "filterType": "EXCHANGE_MAX_ALGO_ORDERS",
                    "maxNumAlgoOrders": 10
                }
            ],
            "symbols": [
                {
                    "symbol": "BTCUSDT",
                    "status": "TRADING",
                    "baseAsset": "BTC",
                    "baseAssetPrecision": 8,
                    "quoteAsset": "USDT",
                    "quotePrecision": 2,
                    "quoteAssetPrecision": 4,
                    "orderTypes": ["LIMIT", "STOP_LOSS"],
                    "icebergAllowed": False,
                    "ocoAllowed": False,
                    "isSpotTradingAllowed": True,
                    "isMarginTradingAllowed": True,
                    "filters": [
                        {
                            "filterType": "PERCENT_PRICE",
                            "multiplierDown": "10.3",
                            "multiplierUp": "10.4",
                            "avgPriceMins": 10
                        },
                        {
                            "filterType": "LOT_SIZE",
                            "minQty": "10.1",
                            "maxQty": "10.4",
                            "stepSize": "1.2"
                        }
                    ],
                    "permissions": ["SPOT", "MARGIN"]
                },
                {
                    "symbol": "BTCUSDT",
                    "status": "TRADING",
                    "baseAsset": "BTC",
                    "baseAssetPrecision": 8,
                    "quoteAsset": "USDT",
                    "quotePrecision": 2,
                    "quoteAssetPrecision": 4,
                    "orderTypes": ["LIMIT", "STOP_LOSS"],
                    "icebergAllowed": False,
                    "ocoAllowed": False,
                    "isSpotTradingAllowed": True,
                    "isMarginTradingAllowed": True,
                    "filters": [
                        {
                            "filterType": "PERCENT_PRICE",
                            "multiplierDown": "10.3",
                            "multiplierUp": "10.4",
                            "avgPriceMins": 10
                        },
                        {
                            "filterType": "LOT_SIZE",
                            "minQty": "10.1",
                            "maxQty": "10.4",
                            "stepSize": "1.2"
                        }
                    ],
                    "permissions": ["SPOT", "MARGIN"]
                }
            ]
        }
        assert await handler.handle_get_exchange_info_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_order_book_ticker_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = BinanceOrderBookTickerModel(
        symbol="BTCUSDT",
        bid_price=Decimal("1500.5"),
        bid_qty=Decimal("24.5"),
        ask_price=Decimal("1600.5"),
        ask_qty=Decimal("30.8"))
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "symbol": "BTCUSDT",
            "bidPrice": "1500.5",
            "bidQty": "24.5",
            "askPrice": "1600.5",
            "askQty": "30.8"
        }
        assert await handler.handle_get_order_book_ticker_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_order_book_tickers_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = [
        BinanceOrderBookTickerModel(
            symbol="BTCUSDT",
            bid_price=Decimal("1500.5"),
            bid_qty=Decimal("24.5"),
            ask_price=Decimal("1600.5"),
            ask_qty=Decimal("30.8")),
        BinanceOrderBookTickerModel(
            symbol="ETHUSDT",
            bid_price=Decimal("1500.5"),
            bid_qty=Decimal("24.5"),
            ask_price=Decimal("1600.5"),
            ask_qty=Decimal("30.8"))
    ]
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
            {
                "symbol": "BTCUSDT",
                "bidPrice": "1500.5",
                "bidQty": "24.5",
                "askPrice": "1600.5",
                "askQty": "30.8"
            },
            {
                "symbol": "ETHUSDT",
                "bidPrice": "1500.5",
                "bidQty": "24.5",
                "askPrice": "1600.5",
                "askQty": "30.8"
            }
        ]
        assert await handler.handle_get_order_book_tickers_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_order_book_response(handler: BinanceMarketDataResponseHandler) -> None:
    orders = [
        BinanceOrderBookOrderModel(
            price=Decimal("1200.5"),
            quantity=Decimal("399.6")),
        BinanceOrderBookOrderModel(
            price=Decimal("1201.5"),
            quantity=Decimal("399.6"))
    ]
    expected = BinanceOrderBookModel(
        last_update_id=123,
        bids=orders,
        asks=orders)

    json_orders: BinanceOrderBookOrdersJson = [
        (
            "1200.5",
            "399.6"
        ),
        (
            "1201.5",
            "399.6"
        )
    ]
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "lastUpdateId": 123,
            "bids": json_orders,
            "asks": json_orders
        }
        assert await handler.handle_get_order_book_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_price_ticker_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = BinancePriceTickerModel(
        symbol="BTCUSDT",
        price=Decimal("157.8"))
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "symbol": "BTCUSDT",
            "price": "157.8"
        }
        assert await handler.handle_get_price_ticker_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_price_tickers_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = [
        BinancePriceTickerModel(
            symbol="BTCUSDT",
            price=Decimal("157.8")),
        BinancePriceTickerModel(
            symbol="ETHUSDT",
            price=Decimal("157.8"))
    ]
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
            {
                "symbol": "BTCUSDT",
                "price": "157.8"
            },
            {
                "symbol": "ETHUSDT",
                "price": "157.8"
            }
        ]
        assert await handler.handle_get_price_tickers_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_ticker_price_change_stat_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = BinanceTickerPriceChangeStatModel(
        symbol="BTCUSDT",
        price_change=Decimal("178.0"),
        weighted_avg_price=Decimal("178.1"),
        prev_close_price=Decimal("178.2"),
        last_price=Decimal("178.3"),
        last_qty=Decimal("178.4"),
        bid_price=Decimal("178.5"),
        ask_price=Decimal("178.6"),
        open_price=Decimal("178.7"),
        high_price=Decimal("178.8"),
        low_price=Decimal("178.9"),
        volume=Decimal("178.11"),
        quote_volume=Decimal("178.12"),
        open_time=123,
        close_time=124,
        first_id=847,
        last_id=838,
        count=158)
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "symbol": "BTCUSDT",
            "priceChange": "178.0",
            "weightedAvgPrice": "178.1",
            "prevClosePrice": "178.2",
            "lastPrice": "178.3",
            "lastQty": "178.4",
            "bidPrice": "178.5",
            "askPrice": "178.6",
            "openPrice": "178.7",
            "highPrice": "178.8",
            "lowPrice": "178.9",
            "volume": "178.11",
            "quoteVolume": "178.12",
            "openTime": 123,
            "closeTime": 124,
            "firstId": 847,
            "lastId": 838,
            "count": 158
        }
        assert await handler.handle_get_ticker_price_change_stat_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_tickers_price_change_stat_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = [
        BinanceTickerPriceChangeStatModel(
            symbol="BTCUSDT",
            price_change=Decimal("178.0"),
            weighted_avg_price=Decimal("178.1"),
            prev_close_price=Decimal("178.2"),
            last_price=Decimal("178.3"),
            last_qty=Decimal("178.4"),
            bid_price=Decimal("178.5"),
            ask_price=Decimal("178.6"),
            open_price=Decimal("178.7"),
            high_price=Decimal("178.8"),
            low_price=Decimal("178.9"),
            volume=Decimal("178.11"),
            quote_volume=Decimal("178.12"),
            open_time=123,
            close_time=124,
            first_id=847,
            last_id=838,
            count=158),
        BinanceTickerPriceChangeStatModel(
            symbol="ETHUSDT",
            price_change=Decimal("178.0"),
            weighted_avg_price=Decimal("178.1"),
            prev_close_price=Decimal("178.2"),
            last_price=Decimal("178.3"),
            last_qty=Decimal("178.4"),
            bid_price=Decimal("178.5"),
            ask_price=Decimal("178.6"),
            open_price=Decimal("178.7"),
            high_price=Decimal("178.8"),
            low_price=Decimal("178.9"),
            volume=Decimal("178.11"),
            quote_volume=Decimal("178.12"),
            open_time=123,
            close_time=124,
            first_id=847,
            last_id=838,
            count=158)
    ]
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
            {
                "symbol": "BTCUSDT",
                "priceChange": "178.0",
                "weightedAvgPrice": "178.1",
                "prevClosePrice": "178.2",
                "lastPrice": "178.3",
                "lastQty": "178.4",
                "bidPrice": "178.5",
                "askPrice": "178.6",
                "openPrice": "178.7",
                "highPrice": "178.8",
                "lowPrice": "178.9",
                "volume": "178.11",
                "quoteVolume": "178.12",
                "openTime": 123,
                "closeTime": 124,
                "firstId": 847,
                "lastId": 838,
                "count": 158
            },
            {
                "symbol": "ETHUSDT",
                "priceChange": "178.0",
                "weightedAvgPrice": "178.1",
                "prevClosePrice": "178.2",
                "lastPrice": "178.3",
                "lastQty": "178.4",
                "bidPrice": "178.5",
                "askPrice": "178.6",
                "openPrice": "178.7",
                "highPrice": "178.8",
                "lowPrice": "178.9",
                "volume": "178.11",
                "quoteVolume": "178.12",
                "openTime": 123,
                "closeTime": 124,
                "firstId": 847,
                "lastId": 838,
                "count": 158
            }
        ]
        assert await handler.handle_get_tickers_price_change_stat_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_trades_response(handler: BinanceMarketDataResponseHandler) -> None:
    expected = [
        BinanceTradeModel(
            id=5,
            price=Decimal("100.3"),
            qty=Decimal("100.4"),
            quote_qty=Decimal("100.5"),
            time=100,
            is_buyer_maker=False,
            is_best_match=True),
        BinanceTradeModel(
            id=6,
            price=Decimal("100.3"),
            qty=Decimal("100.4"),
            quote_qty=Decimal("100.5"),
            time=100,
            is_buyer_maker=False,
            is_best_match=True)
    ]
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
            {
                "id": 5,
                "price": "100.3",
                "qty": "100.4",
                "quoteQty": "100.5",
                "time": 100,
                "isBuyerMaker": False,
                "isBestMatch": True
            },
            {
                "id": 6,
                "price": "100.3",
                "qty": "100.4",
                "quoteQty": "100.5",
                "time": 100,
                "isBuyerMaker": False,
                "isBestMatch": True
            }
        ]
        assert await handler.handle_get_trades_response(mock.Mock()) == expected
