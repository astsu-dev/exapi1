from decimal import Decimal

import pytest
from exapi.models.binance import (BinanceAveragePriceJson,
                                  BinanceAveragePriceModel, BinanceCandleJson,
                                  BinanceCandleModel, BinanceCandles,
                                  BinanceCandlesJson, BinanceFilledOrderJson,
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
                                  BinanceServerTimeJson,
                                  BinanceServerTimeModel,
                                  BinanceTickerPriceChangeStatJson,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTickersPriceChangeStat,
                                  BinanceTickersPriceChangeStatJson,
                                  BinanceTradeJson, BinanceTradeModel,
                                  BinanceTrades, BinanceTradesJson)
from exapi.models.binance.mapper import BinanceModelsMapper


@pytest.fixture(scope="module")
def mapper() -> BinanceModelsMapper:
    return BinanceModelsMapper()


def test_map_to_ping(mapper: BinanceModelsMapper) -> None:
    expected = BinancePingModel()
    json: BinancePingJson = {}
    assert mapper.map_to_ping(json) == expected


def test_map_to_server_time(mapper: BinanceModelsMapper) -> None:
    expected = BinanceServerTimeModel(server_time=1500)
    json: BinanceServerTimeJson = {
        "serverTime": 1500
    }
    assert mapper.map_to_server_time(json) == expected


def test_map_to_average_price(mapper: BinanceModelsMapper) -> None:
    expected = BinanceAveragePriceModel(mins=10, price=Decimal("1500.2"))
    json: BinanceAveragePriceJson = {
        "mins": 10,
        "price": "1500.2"
    }
    assert mapper.map_to_average_price(json) == expected


def test_map_to_candle(mapper: BinanceModelsMapper) -> None:
    expected = BinanceCandleModel(
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
        ignore=Decimal("1500.2"))
    json: BinanceCandleJson = [
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
    ]
    assert mapper.map_to_candle(json) == expected


def test_map_to_candle(mapper: BinanceModelsMapper) -> None:
    expected = BinanceCandleModel(
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
        ignore=Decimal("1500.2"))
    json: BinanceCandleJson = [
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
    ]
    assert mapper.map_to_candle(json) == expected


def test_map_to_candles(mapper: BinanceModelsMapper) -> None:
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
    json: BinanceCandlesJson = [
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
    assert mapper.map_to_candles(json) == expected


def test_map_to_order_book_ticker(mapper: BinanceModelsMapper) -> None:
    expected = BinanceOrderBookTickerModel(
        symbol="BTCUSDT",
        bid_price=Decimal("1500.5"),
        bid_qty=Decimal("24.5"),
        ask_price=Decimal("1600.5"),
        ask_qty=Decimal("30.8"))
    json: BinanceOrderBookTickerJson = {
        "symbol": "BTCUSDT",
        "bidPrice": "1500.5",
        "bidQty": "24.5",
        "askPrice": "1600.5",
        "askQty": "30.8"
    }
    assert mapper.map_to_order_book_ticker(json) == expected


def test_map_to_order_book_tickers(mapper: BinanceModelsMapper) -> None:
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
    json: BinanceOrderBookTickersJson = [
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
    assert mapper.map_to_order_book_tickers(json) == expected


def test_map_to_order_book_order(mapper: BinanceModelsMapper) -> None:
    expected = BinanceOrderBookOrderModel(
        price=Decimal("1200.5"),
        quantity=Decimal("399.6"))
    json: BinanceOrderBookOrderJson = [
        "1200.5",
        "399.6"
    ]
    assert mapper.map_to_order_book_order(json) == expected


def test_map_to_order_book_orders(mapper: BinanceModelsMapper) -> None:
    expected = [
        BinanceOrderBookOrderModel(
            price=Decimal("1200.5"),
            quantity=Decimal("399.6")),
        BinanceOrderBookOrderModel(
            price=Decimal("1201.5"),
            quantity=Decimal("399.6"))
    ]
    json: BinanceOrderBookOrdersJson = [
        (
            "1200.5",
            "399.6"
        ),
        (
            "1201.5",
            "399.6"
        )
    ]
    assert mapper.map_to_order_book_orders(json) == expected


def test_map_to_order_book(mapper: BinanceModelsMapper) -> None:
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
    json: BinanceOrderBookJson = {
        "lastUpdateId": 123,
        "bids": json_orders,
        "asks": json_orders
    }
    assert mapper.map_to_order_book(json) == expected


def test_map_to_filled_order(mapper: BinanceModelsMapper) -> None:
    expected = BinanceFilledOrderModel(
        price=Decimal("127.8"),
        qty=Decimal("700.7"),
        commission=Decimal("10.8"),
        commission_asset="BTC")
    json: BinanceFilledOrderJson = {
        "price": "127.8",
        "qty": "700.7",
        "commission": "10.8",
        "commissionAsset": "BTC"
    }
    assert mapper.map_to_filled_order(json) == expected


def test_map_to_filled_orders(mapper: BinanceModelsMapper) -> None:
    expected = [
        BinanceFilledOrderModel(
            price=Decimal("127.8"),
            qty=Decimal("700.7"),
            commission=Decimal("10.8"),
            commission_asset="BTC"),
        BinanceFilledOrderModel(
            price=Decimal("127.8"),
            qty=Decimal("700.7"),
            commission=Decimal("10.8"),
            commission_asset="ETH")
    ]
    json: BinanceFilledOrdersJson = [
        {
            "price": "127.8",
            "qty": "700.7",
            "commission": "10.8",
            "commissionAsset": "BTC"
        },
        {
            "price": "127.8",
            "qty": "700.7",
            "commission": "10.8",
            "commissionAsset": "ETH"
        }
    ]
    assert mapper.map_to_filled_orders(json) == expected


def test_map_to_order(mapper: BinanceModelsMapper) -> None:
    expected = BinanceOrderModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        transact_time=200,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8"),
        executed_qty=Decimal("18.9"),
        cummulative_quote_qty=Decimal("18.0"),
        status="NEW",
        time_in_force="GTC",
        type="LIMIT",
        side="BUY",
        fills=[
            BinanceFilledOrderModel(
                price=Decimal("127.8"),
                qty=Decimal("700.7"),
                commission=Decimal("10.8"),
                commission_asset="BTC"),
            BinanceFilledOrderModel(
                price=Decimal("127.8"),
                qty=Decimal("700.7"),
                commission=Decimal("10.8"),
                commission_asset="ETH")
        ]
    )
    json: BinanceOrderJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "transactTime": 200,
        "price": "18.7",
        "origQty": "18.8",
        "executedQty": "18.9",
        "cummulativeQuoteQty": "18.0",
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "fills": [
            {
                "price": "127.8",
                "qty": "700.7",
                "commission": "10.8",
                "commissionAsset": "BTC"
            },
            {
                "price": "127.8",
                "qty": "700.7",
                "commission": "10.8",
                "commissionAsset": "ETH"
            }
        ]
    }
    assert mapper.map_to_order(json) == expected


def test_map_to_orders(mapper: BinanceModelsMapper) -> None:
    expected = [
        BinanceOrderModel(
            symbol="BTCUSDT",
            order_id=1234,
            order_list_id=1235,
            client_order_id="11cc",
            transact_time=200,
            price=Decimal("18.7"),
            orig_qty=Decimal("18.8"),
            executed_qty=Decimal("18.9"),
            cummulative_quote_qty=Decimal("18.0"),
            status="NEW",
            time_in_force="GTC",
            type="LIMIT",
            side="BUY",
            fills=[
                BinanceFilledOrderModel(
                    price=Decimal("127.8"),
                    qty=Decimal("700.7"),
                    commission=Decimal("10.8"),
                    commission_asset="BTC"),
                BinanceFilledOrderModel(
                    price=Decimal("127.8"),
                    qty=Decimal("700.7"),
                    commission=Decimal("10.8"),
                    commission_asset="ETH")
            ]
        ),
        BinanceOrderModel(
            symbol="ETHUSDT",
            order_id=1234,
            order_list_id=1235,
            client_order_id="11cc",
            transact_time=200,
            price=Decimal("18.7"),
            orig_qty=Decimal("18.8"),
            executed_qty=Decimal("18.9"),
            cummulative_quote_qty=Decimal("18.0"),
            status="NEW",
            time_in_force="GTC",
            type="LIMIT",
            side="BUY",
            fills=[
                BinanceFilledOrderModel(
                    price=Decimal("127.8"),
                    qty=Decimal("700.7"),
                    commission=Decimal("10.8"),
                    commission_asset="BTC"),
                BinanceFilledOrderModel(
                    price=Decimal("127.8"),
                    qty=Decimal("700.7"),
                    commission=Decimal("10.8"),
                    commission_asset="ETH")
            ]
        )
    ]
    json: BinanceOrdersJson = [
        {
            "symbol": "BTCUSDT",
            "orderId": 1234,
            "orderListId": 1235,
            "clientOrderId": "11cc",
            "transactTime": 200,
            "price": "18.7",
            "origQty": "18.8",
            "executedQty": "18.9",
            "cummulativeQuoteQty": "18.0",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "BUY",
            "fills": [
                {
                    "price": "127.8",
                    "qty": "700.7",
                    "commission": "10.8",
                    "commissionAsset": "BTC"
                },
                {
                    "price": "127.8",
                    "qty": "700.7",
                    "commission": "10.8",
                    "commissionAsset": "ETH"
                }
            ]
        },
        {
            "symbol": "ETHUSDT",
            "orderId": 1234,
            "orderListId": 1235,
            "clientOrderId": "11cc",
            "transactTime": 200,
            "price": "18.7",
            "origQty": "18.8",
            "executedQty": "18.9",
            "cummulativeQuoteQty": "18.0",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "BUY",
            "fills": [
                {
                    "price": "127.8",
                    "qty": "700.7",
                    "commission": "10.8",
                    "commissionAsset": "BTC"
                },
                {
                    "price": "127.8",
                    "qty": "700.7",
                    "commission": "10.8",
                    "commissionAsset": "ETH"
                }
            ]
        }
    ]
    assert mapper.map_to_orders(json) == expected


def test_map_to_price_ticker(mapper: BinanceModelsMapper) -> None:
    expected = BinancePriceTickerModel(
        symbol="BTCUSDT",
        price=Decimal("157.8"))
    json: BinancePriceTickerJson = {
        "symbol": "BTCUSDT",
        "price": "157.8"
    }
    assert mapper.map_to_price_ticker(json) == expected


def test_map_to_price_tickers(mapper: BinanceModelsMapper) -> None:
    expected = [
        BinancePriceTickerModel(
            symbol="BTCUSDT",
            price=Decimal("157.8")),
        BinancePriceTickerModel(
            symbol="ETHUSDT",
            price=Decimal("157.8"))
    ]
    json: BinancePriceTickersJson = [
        {
            "symbol": "BTCUSDT",
            "price": "157.8"
        },
        {
            "symbol": "ETHUSDT",
            "price": "157.8"
        }
    ]
    assert mapper.map_to_price_tickers(json) == expected


def test_map_to_ticker_price_change_stat(mapper: BinanceModelsMapper) -> None:
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
    json: BinanceTickerPriceChangeStatJson = {
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
    assert mapper.map_to_ticker_price_change_stat(json) == expected


def test_map_to_tickers_price_change_stat(mapper: BinanceModelsMapper) -> None:
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
    json: BinanceTickersPriceChangeStatJson = [
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
    assert mapper.map_to_tickers_price_change_stat(json) == expected


def test_map_to_trade(mapper: BinanceModelsMapper) -> None:
    expected = BinanceTradeModel(
        id=5,
        price=Decimal("100.3"),
        qty=Decimal("100.4"),
        quote_qty=Decimal("100.5"),
        time=100,
        is_buyer_maker=False,
        is_best_match=True)
    json: BinanceTradeJson = {
        "id": 5,
        "price": "100.3",
        "qty": "100.4",
        "quoteQty": "100.5",
        "time": 100,
        "isBuyerMaker": False,
        "isBestMatch": True
    }
    assert mapper.map_to_trade(json) == expected


def test_map_to_trades(mapper: BinanceModelsMapper) -> None:
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
    json: BinanceTradesJson = [
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
    assert mapper.map_to_trades(json) == expected
