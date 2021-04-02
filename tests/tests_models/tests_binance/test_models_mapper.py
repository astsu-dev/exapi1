from decimal import Decimal

import pytest
from exapi.models.binance import (BinanceAccountInfoJson,
                                  BinanceAccountInfoModel,
                                  BinanceAccountTradeJson,
                                  BinanceAccountTradeModel,
                                  BinanceAccountTradesJson,
                                  BinanceAggregateTradeJson,
                                  BinanceAggregateTradeModel,
                                  BinanceAggregateTradesJson,
                                  BinanceAveragePriceJson,
                                  BinanceAveragePriceModel, BinanceCandleJson,
                                  BinanceCandleModel, BinanceCandlesJson,
                                  BinanceCurrencyBalanceJson,
                                  BinanceCurrencyBalanceModel,
                                  BinanceCurrencyBalancesJson,
                                  BinanceErrorJson, BinanceErrorModel,
                                  BinanceExchangeFilterJson,
                                  BinanceExchangeFilterModel,
                                  BinanceExchangeFilters,
                                  BinanceExchangeFiltersJson,
                                  BinanceExchangeInfoJson,
                                  BinanceExchangeInfoModel,
                                  BinanceFilledOrderJson,
                                  BinanceFilledOrderModel,
                                  BinanceFilledOrdersJson,
                                  BinanceIcebergPartsSymbolFilterJson,
                                  BinanceIcebergPartsSymbolFilterModel,
                                  BinanceLotSizeSymbolFilterJson,
                                  BinanceLotSizeSymbolFilterModel,
                                  BinanceMarketLotSizeSymbolFilterJson,
                                  BinanceMarketLotSizeSymbolFilterModel,
                                  BinanceMaxNumAlgoOrdersExchangeFilterModel,
                                  BinanceMaxNumAlgoOrdersSymbolFilterJson,
                                  BinanceMaxNumAlgoOrdersSymbolFilterModel,
                                  BinanceMaxNumIcebergOrdersSymbolFilterJson,
                                  BinanceMaxNumIcebergOrdersSymbolFilterModel,
                                  BinanceMaxNumOrdersExchangeFilterJson,
                                  BinanceMaxNumOrdersExchangeFilterModel,
                                  BinanceMaxNumOrdersSymbolFilterJson,
                                  BinanceMaxNumOrdersSymbolFilterModel,
                                  BinanceMaxPositionSymbolFilterJson,
                                  BinanceMaxPositionSymbolFilterModel,
                                  BinanceMinNotionalSymbolFilterJson,
                                  BinanceMinNotionalSymbolFilterModel,
                                  BinanceOrderBookJson, BinanceOrderBookModel,
                                  BinanceOrderBookOrderJson,
                                  BinanceOrderBookOrderModel,
                                  BinanceOrderBookOrdersJson,
                                  BinanceOrderBookTickerJson,
                                  BinanceOrderBookTickerModel,
                                  BinanceOrderBookTickersJson,
                                  BinanceOrderInfoJson, BinanceOrderInfoModel,
                                  BinanceOrderInfosJson, BinanceOrderModel,
                                  BinanceOrdersJson,
                                  BinanceOrdersRateLimitJson,
                                  BinanceOrdersRateLimitModel,
                                  BinancePercentPriceSymbolFilterJson,
                                  BinancePercentPriceSymbolFilterModel,
                                  BinancePingJson, BinancePingModel,
                                  BinancePriceTickerJson,
                                  BinancePriceTickerModel,
                                  BinancePriceTickersJson,
                                  BinanceRateLimitJson, BinanceRateLimitModel,
                                  BinanceRawRequestsRateLimitJson,
                                  BinanceRawRequestsRateLimitModel,
                                  BinanceRequestWeightRateLimitJson,
                                  BinanceRequestWeightRateLimitModel,
                                  BinanceServerTimeJson,
                                  BinanceServerTimeModel,
                                  BinanceSymbolFilterJson,
                                  BinanceSymbolFilterModel,
                                  BinanceSymbolFilters,
                                  BinanceSymbolFiltersJson, BinanceSymbolJson,
                                  BinanceSymbolModel, BinanceSymbolsJson,
                                  BinanceTickerPriceChangeStatJson,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTickersPriceChangeStatJson,
                                  BinanceTradeJson, BinanceTradeModel,
                                  BinanceTradesJson)
from exapi.models.binance.mapper import BinanceModelsMapper
from exapi.models.binance.order import (BinanceOrderJson, BinanceTestOrderJson,
                                        BinanceTestOrderModel)


@pytest.fixture(scope="module")
def mapper() -> BinanceModelsMapper:
    return BinanceModelsMapper()


def test_map_to_error(mapper: BinanceModelsMapper) -> None:
    expected = BinanceErrorModel(code=-1001, msg="Not enough money.")
    json: BinanceErrorJson = {
        "code": -1001,
        "msg": "Not enough money."
    }
    assert mapper.map_to_error(json) == expected


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
    json: BinanceCandleJson = (
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
    )
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
    json: BinanceOrderBookOrderJson = (
        "1200.5",
        "399.6"
    )
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


def test_map_to_test_order(mapper: BinanceModelsMapper) -> None:
    expected = BinanceTestOrderModel()
    json: BinanceTestOrderJson = {}
    assert mapper.map_to_test_order(json) == expected


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


def test_map_to_aggregate_trade(mapper: BinanceModelsMapper) -> None:
    expected = BinanceAggregateTradeModel(
        id=5,
        price=Decimal("10.5"),
        qty=Decimal("10.3"),
        first_id=52,
        last_id=57,
        time=1005,
        is_buyer_maker=True,
        is_best_match=False)
    json: BinanceAggregateTradeJson = {
        "a": 5,
        "p": "10.5",
        "q": "10.3",
        "f": 52,
        "l": 57,
        "T": 1005,
        "m": True,
        "M": False
    }
    assert mapper.map_to_aggregate_trade(json) == expected


def test_map_to_aggregate_trades(mapper: BinanceModelsMapper) -> None:
    expected = [
        BinanceAggregateTradeModel(
            id=5,
            price=Decimal("10.5"),
            qty=Decimal("10.3"),
            first_id=52,
            last_id=57,
            time=1005,
            is_buyer_maker=True,
            is_best_match=False),
        BinanceAggregateTradeModel(
            id=6,
            price=Decimal("10.5"),
            qty=Decimal("10.3"),
            first_id=52,
            last_id=57,
            time=1005,
            is_buyer_maker=True,
            is_best_match=False)
    ]
    json: BinanceAggregateTradesJson = [
        {
            "a": 5,
            "p": "10.5",
            "q": "10.3",
            "f": 52,
            "l": 57,
            "T": 1005,
            "m": True,
            "M": False
        },
        {
            "a": 6,
            "p": "10.5",
            "q": "10.3",
            "f": 52,
            "l": 57,
            "T": 1005,
            "m": True,
            "M": False
        }
    ]
    assert mapper.map_to_aggregate_trades(json) == expected


def test_map_to_percent_price_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinancePercentPriceSymbolFilterModel(
        filter_type="PERCENT_PRICE",
        multiplier_up=Decimal("20.4"),
        multiplier_down=Decimal("20.3"),
        avg_price_mins=10)
    json: BinancePercentPriceSymbolFilterJson = {
        "filterType": "PERCENT_PRICE",
        "multiplierUp": "20.4",
        "multiplierDown": "20.3",
        "avgPriceMins": 10
    }
    assert mapper.map_to_percent_price_symbol_filter(json) == expected


def test_map_to_lot_size_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceLotSizeSymbolFilterModel(
        filter_type="LOT_SIZE",
        min_qty=Decimal("20.4"),
        max_qty=Decimal("20.3"),
        step_size=Decimal("5.3"))
    json: BinanceLotSizeSymbolFilterJson = {
        "filterType": "LOT_SIZE",
        "minQty": "20.4",
        "maxQty": "20.3",
        "stepSize": "5.3"
    }
    assert mapper.map_to_lot_size_symbol_filter(json) == expected


def test_map_to_min_notional_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceMinNotionalSymbolFilterModel(
        filter_type="MIN_NOTIONAL",
        min_notional=Decimal("10.3"),
        apply_to_market=True,
        avg_price_mins=10)
    json: BinanceMinNotionalSymbolFilterJson = {
        "filterType": "MIN_NOTIONAL",
        "minNotional": "10.3",
        "applyToMarket": True,
        "avgPriceMins": 10
    }
    assert mapper.map_to_min_notional_symbol_filter(json) == expected


def test_map_to_iceberg_parts_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceIcebergPartsSymbolFilterModel(
        filter_type="ICEBERG_PARTS",
        limit=10)
    json: BinanceIcebergPartsSymbolFilterJson = {
        "filterType": "ICEBERG_PARTS",
        "limit": 10
    }
    assert mapper.map_to_iceberg_parts_symbol_filter(json) == expected


def test_map_to_market_lot_size_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceMarketLotSizeSymbolFilterModel(
        filter_type="MARKET_LOT_SIZE",
        min_qty=Decimal("20.4"),
        max_qty=Decimal("20.3"),
        step_size=Decimal("5.3"))
    json: BinanceMarketLotSizeSymbolFilterJson = {
        "filterType": "MARKET_LOT_SIZE",
        "minQty": "20.4",
        "maxQty": "20.3",
        "stepSize": "5.3"
    }
    assert mapper.map_to_market_lot_size_symbol_filter(json) == expected


def test_map_to_max_num_orders_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceMaxNumOrdersSymbolFilterModel(
        filter_type="MAX_NUM_ORDERS",
        max_num_orders=10)
    json: BinanceMaxNumOrdersSymbolFilterJson = {
        "filterType": "MAX_NUM_ORDERS",
        "maxNumOrders": 10
    }
    assert mapper.map_to_max_num_orders_symbol_filter(json) == expected


def test_map_to_max_num_algo_orders_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceMaxNumAlgoOrdersSymbolFilterModel(
        filter_type="MAX_NUM_ALGO_ORDERS",
        max_num_algo_orders=10)
    json: BinanceMaxNumAlgoOrdersSymbolFilterJson = {
        "filterType": "MAX_NUM_ALGO_ORDERS",
        "maxNumAlgoOrders": 10
    }
    assert mapper.map_to_max_num_algo_orders_symbol_filter(json) == expected


def test_map_to_max_num_iceberg_orders_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceMaxNumIcebergOrdersSymbolFilterModel(
        filter_type="MAX_NUM_ICEBERG_ORDERS",
        max_num_iceberg_orders=10)
    json: BinanceMaxNumIcebergOrdersSymbolFilterJson = {
        "filterType": "MAX_NUM_ICEBERG_ORDERS",
        "maxNumIcebergOrders": 10
    }
    assert mapper.map_to_max_num_iceberg_orders_symbol_filter(json) == expected


def test_map_to_max_position_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceMaxPositionSymbolFilterModel(
        filter_type="MAX_POSITION",
        max_position=Decimal("10.3"))
    json: BinanceMaxPositionSymbolFilterJson = {
        "filterType": "MAX_POSITION",
        "maxPosition": "10.3"
    }
    assert mapper.map_to_max_position_symbol_filter(json) == expected


def test_map_symbol_filter(mapper: BinanceModelsMapper) -> None:
    expected: BinanceSymbolFilterModel
    json: BinanceSymbolFilterJson

    expected = BinancePercentPriceSymbolFilterModel(
        filter_type="PERCENT_PRICE",
        multiplier_up=Decimal("20.4"),
        multiplier_down=Decimal("20.3"),
        avg_price_mins=10)
    json = {
        "filterType": "PERCENT_PRICE",
        "multiplierUp": "20.4",
        "multiplierDown": "20.3",
        "avgPriceMins": 10
    }
    assert mapper.map_to_symbol_filter(json) == expected

    expected = BinanceLotSizeSymbolFilterModel(
        filter_type="LOT_SIZE",
        min_qty=Decimal("20.4"),
        max_qty=Decimal("20.3"),
        step_size=Decimal("5.3"))
    json = {
        "filterType": "LOT_SIZE",
        "minQty": "20.4",
        "maxQty": "20.3",
        "stepSize": "5.3"
    }
    assert mapper.map_to_symbol_filter(json) == expected

    expected = BinanceMinNotionalSymbolFilterModel(
        filter_type="MIN_NOTIONAL",
        min_notional=Decimal("10.3"),
        apply_to_market=True,
        avg_price_mins=10)
    json = {
        "filterType": "MIN_NOTIONAL",
        "minNotional": "10.3",
        "applyToMarket": True,
        "avgPriceMins": 10
    }
    assert mapper.map_to_symbol_filter(json) == expected

    expected = BinanceIcebergPartsSymbolFilterModel(
        filter_type="ICEBERG_PARTS",
        limit=10)
    json = {
        "filterType": "ICEBERG_PARTS",
        "limit": 10
    }
    assert mapper.map_to_symbol_filter(json) == expected

    expected = BinanceMarketLotSizeSymbolFilterModel(
        filter_type="MARKET_LOT_SIZE",
        min_qty=Decimal("20.4"),
        max_qty=Decimal("20.3"),
        step_size=Decimal("5.3"))
    json = {
        "filterType": "MARKET_LOT_SIZE",
        "minQty": "20.4",
        "maxQty": "20.3",
        "stepSize": "5.3"
    }
    assert mapper.map_to_symbol_filter(json) == expected

    expected = BinanceMaxNumOrdersSymbolFilterModel(
        filter_type="MAX_NUM_ORDERS",
        max_num_orders=10)
    json = {
        "filterType": "MAX_NUM_ORDERS",
        "maxNumOrders": 10
    }
    assert mapper.map_to_symbol_filter(json) == expected

    expected = BinanceMaxNumAlgoOrdersSymbolFilterModel(
        filter_type="MAX_NUM_ALGO_ORDERS",
        max_num_algo_orders=10)
    json = {
        "filterType": "MAX_NUM_ALGO_ORDERS",
        "maxNumAlgoOrders": 10
    }
    assert mapper.map_to_symbol_filter(json) == expected

    expected = BinanceMaxNumIcebergOrdersSymbolFilterModel(
        filter_type="MAX_NUM_ICEBERG_ORDERS",
        max_num_iceberg_orders=10)
    json = {
        "filterType": "MAX_NUM_ICEBERG_ORDERS",
        "maxNumIcebergOrders": 10
    }
    assert mapper.map_to_symbol_filter(json) == expected

    expected = BinanceMaxPositionSymbolFilterModel(
        filter_type="MAX_POSITION",
        max_position=Decimal("10.3"))
    json = {
        "filterType": "MAX_POSITION",
        "maxPosition": "10.3"
    }
    assert mapper.map_to_symbol_filter(json) == expected

    json = {
        "filterType": "AA"
    }
    with pytest.raises(AssertionError):
        mapper.map_to_symbol_filter(json)


def test_map_symbol_filters(mapper: BinanceModelsMapper) -> None:
    expected: BinanceSymbolFilters
    json: BinanceSymbolFiltersJson

    expected = [
        BinancePercentPriceSymbolFilterModel(
            filter_type="PERCENT_PRICE",
            multiplier_up=Decimal("20.4"),
            multiplier_down=Decimal("20.3"),
            avg_price_mins=10),
        BinanceLotSizeSymbolFilterModel(
            filter_type="LOT_SIZE",
            min_qty=Decimal("20.4"),
            max_qty=Decimal("20.3"),
            step_size=Decimal("5.3")),
        BinanceMinNotionalSymbolFilterModel(
            filter_type="MIN_NOTIONAL",
            min_notional=Decimal("10.3"),
            apply_to_market=True,
            avg_price_mins=10),
        BinanceIcebergPartsSymbolFilterModel(
            filter_type="ICEBERG_PARTS",
            limit=10),
        BinanceMarketLotSizeSymbolFilterModel(
            filter_type="MARKET_LOT_SIZE",
            min_qty=Decimal("20.4"),
            max_qty=Decimal("20.3"),
            step_size=Decimal("5.3")),
        BinanceMaxNumOrdersSymbolFilterModel(
            filter_type="MAX_NUM_ORDERS",
            max_num_orders=10),
        BinanceMaxNumAlgoOrdersSymbolFilterModel(
            filter_type="MAX_NUM_ALGO_ORDERS",
            max_num_algo_orders=10),
        BinanceMaxNumIcebergOrdersSymbolFilterModel(
            filter_type="MAX_NUM_ICEBERG_ORDERS",
            max_num_iceberg_orders=10),
        BinanceMaxPositionSymbolFilterModel(
            filter_type="MAX_POSITION",
            max_position=Decimal("10.3"))
    ]
    json = [
        {
            "filterType": "PERCENT_PRICE",
            "multiplierUp": "20.4",
            "multiplierDown": "20.3",
            "avgPriceMins": 10
        },
        {
            "filterType": "LOT_SIZE",
            "minQty": "20.4",
            "maxQty": "20.3",
            "stepSize": "5.3"
        },
        {
            "filterType": "MIN_NOTIONAL",
            "minNotional": "10.3",
            "applyToMarket": True,
            "avgPriceMins": 10
        },
        {
            "filterType": "ICEBERG_PARTS",
            "limit": 10
        },
        {
            "filterType": "MARKET_LOT_SIZE",
            "minQty": "20.4",
            "maxQty": "20.3",
            "stepSize": "5.3"
        },
        {
            "filterType": "MAX_NUM_ORDERS",
            "maxNumOrders": 10
        },
        {
            "filterType": "MAX_NUM_ALGO_ORDERS",
            "maxNumAlgoOrders": 10
        },
        {
            "filterType": "MAX_NUM_ICEBERG_ORDERS",
            "maxNumIcebergOrders": 10
        },
        {
            "filterType": "MAX_POSITION",
            "maxPosition": "10.3"
        }
    ]

    assert mapper.map_to_symbol_filters(json) == expected

    json = [
        {
            "filterType": "AA"
        }
    ]
    with pytest.raises(AssertionError):
        mapper.map_to_symbol_filters(json)

    json = []
    expected = []
    assert mapper.map_to_symbol_filters(json) == expected


def test_map_to_symbol(mapper: BinanceModelsMapper) -> None:
    expected = BinanceSymbolModel(
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
    json: BinanceSymbolJson = {
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

    assert mapper.map_to_symbol(json) == expected


def test_map_to_symbols(mapper: BinanceModelsMapper) -> None:
    expected = [
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
    ]
    json: BinanceSymbolsJson = [
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

    assert mapper.map_to_symbols(json) == expected

    expected = []
    json = []

    assert mapper.map_to_symbols(json) == expected


def test_map_to_max_num_orders_exchange_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceMaxNumOrdersExchangeFilterModel(
        filter_type="EXCHANGE_MAX_NUM_ORDERS",
        max_num_orders=10)
    json: BinanceMaxNumOrdersExchangeFilterJson = {
        "filterType": "EXCHANGE_MAX_NUM_ORDERS",
        "maxNumOrders": 10
    }

    assert mapper.map_to_max_num_orders_exchange_filter(json) == expected


def test_map_to_max_num_algo_orders_exchange_filter(mapper: BinanceModelsMapper) -> None:
    expected = BinanceMaxNumAlgoOrdersExchangeFilterModel(
        filter_type="EXCHANGE_MAX_ALGO_ORDERS",
        max_num_algo_orders=10)
    json: BinanceMaxNumAlgoOrdersExchangeFilterModel = {
        "filterType": "EXCHANGE_MAX_ALGO_ORDERS",
        "maxNumAlgoOrders": 10
    }

    assert mapper.map_to_max_num_algo_orders_exchange_filter(json) == expected


def test_map_to_exchange_filter(mapper: BinanceModelsMapper) -> None:
    expected: BinanceExchangeFilterModel
    json: BinanceExchangeFilterJson

    expected = BinanceMaxNumOrdersExchangeFilterModel(
        filter_type="EXCHANGE_MAX_NUM_ORDERS",
        max_num_orders=10)
    json = {
        "filterType": "EXCHANGE_MAX_NUM_ORDERS",
        "maxNumOrders": 10
    }
    assert mapper.map_to_exchange_filter(json) == expected

    expected = BinanceMaxNumAlgoOrdersExchangeFilterModel(
        filter_type="EXCHANGE_MAX_ALGO_ORDERS",
        max_num_algo_orders=10)
    json = {
        "filterType": "EXCHANGE_MAX_ALGO_ORDERS",
        "maxNumAlgoOrders": 10
    }
    assert mapper.map_to_exchange_filter(json) == expected

    json = {"filterType": "aa"}
    with pytest.raises(AssertionError):
        mapper.map_to_exchange_filter(json)


def test_map_to_exchange_filters(mapper: BinanceModelsMapper) -> None:
    expected: BinanceExchangeFilters
    json: BinanceExchangeFiltersJson

    expected = [
        BinanceMaxNumOrdersExchangeFilterModel(
            filter_type="EXCHANGE_MAX_NUM_ORDERS",
            max_num_orders=10),
        BinanceMaxNumAlgoOrdersExchangeFilterModel(
            filter_type="EXCHANGE_MAX_ALGO_ORDERS",
            max_num_algo_orders=10)
    ]
    json = [
        {
            "filterType": "EXCHANGE_MAX_NUM_ORDERS",
            "maxNumOrders": 10
        },
        {
            "filterType": "EXCHANGE_MAX_ALGO_ORDERS",
            "maxNumAlgoOrders": 10
        }
    ]
    assert mapper.map_to_exchange_filters(json) == expected

    expected = []
    json = []
    assert mapper.map_to_exchange_filters(json) == expected


def test_map_to_request_weight_rate_limit(mapper: BinanceModelsMapper) -> None:
    expected = BinanceRequestWeightRateLimitModel(
        rate_limit_type="REQUEST_WEIGHT",
        interval="SECOND",
        interval_num=10,
        limit=20)
    json: BinanceRequestWeightRateLimitJson = {
        "rateLimitType": "REQUEST_WEIGHT",
        "interval": "SECOND",
        "intervalNum": 10,
        "limit": 20
    }

    assert mapper.map_to_request_weight_rate_limit(json) == expected


def test_map_to_orders_rate_limit(mapper: BinanceModelsMapper) -> None:
    expected = BinanceOrdersRateLimitModel(
        rate_limit_type="ORDERS",
        interval="SECOND",
        interval_num=10,
        limit=20)
    json: BinanceOrdersRateLimitJson = {
        "rateLimitType": "ORDERS",
        "interval": "SECOND",
        "intervalNum": 10,
        "limit": 20
    }

    assert mapper.map_to_orders_rate_limit(json) == expected


def test_map_to_raw_requests_rate_limit(mapper: BinanceModelsMapper) -> None:
    expected = BinanceRawRequestsRateLimitModel(
        rate_limit_type="RAW_REQUESTS",
        interval="SECOND",
        interval_num=10,
        limit=20)
    json: BinanceRawRequestsRateLimitJson = {
        "rateLimitType": "RAW_REQUESTS",
        "interval": "SECOND",
        "intervalNum": 10,
        "limit": 20
    }

    assert mapper.map_to_raw_requests_rate_limit(json) == expected


def test_map_to_rate_limit(mapper: BinanceModelsMapper) -> None:
    expected: BinanceRateLimitModel
    json: BinanceRateLimitJson

    expected = BinanceRequestWeightRateLimitModel(
        rate_limit_type="REQUEST_WEIGHT",
        interval="SECOND",
        interval_num=10,
        limit=20)
    json = {
        "rateLimitType": "REQUEST_WEIGHT",
        "interval": "SECOND",
        "intervalNum": 10,
        "limit": 20
    }
    assert mapper.map_to_rate_limit(json) == expected

    expected = BinanceOrdersRateLimitModel(
        rate_limit_type="ORDERS",
        interval="SECOND",
        interval_num=10,
        limit=20)
    json = {
        "rateLimitType": "ORDERS",
        "interval": "SECOND",
        "intervalNum": 10,
        "limit": 20
    }
    assert mapper.map_to_rate_limit(json) == expected

    expected = BinanceRawRequestsRateLimitModel(
        rate_limit_type="RAW_REQUESTS",
        interval="SECOND",
        interval_num=10,
        limit=20)
    json = {
        "rateLimitType": "RAW_REQUESTS",
        "interval": "SECOND",
        "intervalNum": 10,
        "limit": 20
    }
    assert mapper.map_to_rate_limit(json) == expected


def test_map_to_rate_limits(mapper: BinanceModelsMapper) -> None:
    expected: BinanceRateLimitModel
    json: BinanceRateLimitJson

    expected = [
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
    ]
    json = [
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
    ]
    assert mapper.map_to_rate_limits(json) == expected

    expected = []
    json = []
    assert mapper.map_to_rate_limits(json) == expected


def test_map_to_exchange_info(mapper: BinanceModelsMapper) -> None:
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
    json: BinanceExchangeInfoJson = {
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

    assert mapper.map_to_exchange_info(json) == expected


def test_map_to_balance(mapper: BinanceModelsMapper) -> None:
    expected = BinanceCurrencyBalanceModel(
        asset="BTC",
        free=Decimal("10.2"),
        locked=Decimal("1.1"))
    json: BinanceCurrencyBalanceJson = {
        "asset": "BTC",
        "free": "10.2",
        "locked": "1.1"
    }
    assert mapper.map_to_balance(json) == expected


def test_map_to_balances(mapper: BinanceModelsMapper) -> None:
    expected = [
        BinanceCurrencyBalanceModel(
            asset="BTC",
            free=Decimal("10.2"),
            locked=Decimal("1.1")),
        BinanceCurrencyBalanceModel(
            asset="ETH",
            free=Decimal("10.2"),
            locked=Decimal("1.1"))
    ]
    json: BinanceCurrencyBalancesJson = [
        {
            "asset": "BTC",
            "free": "10.2",
            "locked": "1.1"
        },
        {
            "asset": "ETH",
            "free": "10.2",
            "locked": "1.1"
        }
    ]
    assert mapper.map_to_balances(json) == expected

    expected = []
    json = []
    assert mapper.map_to_balances(json) == expected


def test_map_to_account_info(mapper: BinanceModelsMapper) -> None:
    expected = BinanceAccountInfoModel(
        maker_commission=10,
        taker_commission=15,
        buyer_commission=11,
        seller_commission=12,
        can_trade=True,
        can_withdraw=True,
        can_deposit=False,
        update_time=500,
        account_type="SPOT",
        balances=[
            BinanceCurrencyBalanceModel(
                asset="BTC",
                free=Decimal("10.2"),
                locked=Decimal("1.1")),
            BinanceCurrencyBalanceModel(
                asset="ETH",
                free=Decimal("10.2"),
                locked=Decimal("1.1"))
        ]
    )
    json: BinanceAccountInfoJson = {
        "makerCommission": 10,
        "takerCommission": 15,
        "buyerCommission": 11,
        "sellerCommission": 12,
        "canTrade": True,
        "canWithdraw": True,
        "canDeposit": False,
        "updateTime": 500,
        "accountType": "SPOT",
        "balances": [
            {
                "asset": "BTC",
                "free": "10.2",
                "locked": "1.1"
            },
            {
                "asset": "ETH",
                "free": "10.2",
                "locked": "1.1"
            }
        ]
    }

    assert mapper.map_to_account_info(json) == expected


def test_map_to_order_info(mapper: BinanceModelsMapper) -> None:
    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7")
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7"
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8")
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7",
        "origQty": "18.8"
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8"),
        executed_qty=Decimal("18.9")
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7",
        "origQty": "18.8",
        "executedQty": "18.9"
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8"),
        executed_qty=Decimal("18.9"),
        cummulative_quote_qty=Decimal("18.0")
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7",
        "origQty": "18.8",
        "executedQty": "18.9",
        "cummulativeQuoteQty": "18.0"
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8"),
        executed_qty=Decimal("18.9"),
        cummulative_quote_qty=Decimal("18.0"),
        status="NEW"
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7",
        "origQty": "18.8",
        "executedQty": "18.9",
        "cummulativeQuoteQty": "18.0",
        "status": "NEW"
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8"),
        executed_qty=Decimal("18.9"),
        cummulative_quote_qty=Decimal("18.0"),
        status="NEW",
        time_in_force="GTC"
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7",
        "origQty": "18.8",
        "executedQty": "18.9",
        "cummulativeQuoteQty": "18.0",
        "status": "NEW",
        "timeInForce": "GTC"
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8"),
        executed_qty=Decimal("18.9"),
        cummulative_quote_qty=Decimal("18.0"),
        status="NEW",
        time_in_force="GTC",
        type="LIMIT"
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7",
        "origQty": "18.8",
        "executedQty": "18.9",
        "cummulativeQuoteQty": "18.0",
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT"
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8"),
        executed_qty=Decimal("18.9"),
        cummulative_quote_qty=Decimal("18.0"),
        status="NEW",
        time_in_force="GTC",
        type="LIMIT",
        side="BUY"
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7",
        "origQty": "18.8",
        "executedQty": "18.9",
        "cummulativeQuoteQty": "18.0",
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY"
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8"),
        executed_qty=Decimal("18.9"),
        cummulative_quote_qty=Decimal("18.0"),
        status="NEW",
        time_in_force="GTC",
        type="LIMIT",
        side="BUY",
        orig_quote_order_qty=Decimal("15000")
    )
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7",
        "origQty": "18.8",
        "executedQty": "18.9",
        "cummulativeQuoteQty": "18.0",
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "origQuoteOrderQty": "15000"
    }
    assert mapper.map_to_order_info(json) == expected

    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500,
        price=Decimal("18.7"),
        orig_qty=Decimal("18.8"),
        executed_qty=Decimal("18.9"),
        cummulative_quote_qty=Decimal("18.0"),
        status="NEW",
        time_in_force="GTC",
        type="LIMIT",
        side="BUY",
        orig_quote_order_qty=Decimal("15000"),
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
    json: BinanceOrderInfoJson = {
        "symbol": "BTCUSDT",
        "orderId": 1234,
        "orderListId": 1235,
        "clientOrderId": "11cc",
        "isWorking": True,
        "updateTime": 1500,
        "price": "18.7",
        "origQty": "18.8",
        "executedQty": "18.9",
        "cummulativeQuoteQty": "18.0",
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "origQuoteOrderQty": "15000",
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
    assert mapper.map_to_order_info(json) == expected


def test_map_to_order_infos(mapper: BinanceModelsMapper) -> None:
    expected = [
        BinanceOrderInfoModel(
            symbol="BTCUSDT",
            order_id=1234,
            order_list_id=1235,
            client_order_id="11cc",
            is_working=True,
            update_time=1500),
        BinanceOrderInfoModel(
            symbol="ETHUSDT",
            order_id=1234,
            order_list_id=1235,
            client_order_id="11cc",
            is_working=True,
            update_time=1500)
    ]
    json: BinanceOrderInfosJson = [
        {
            "symbol": "BTCUSDT",
            "orderId": 1234,
            "orderListId": 1235,
            "clientOrderId": "11cc",
            "isWorking": True,
            "updateTime": 1500
        },
        {
            "symbol": "ETHUSDT",
            "orderId": 1234,
            "orderListId": 1235,
            "clientOrderId": "11cc",
            "isWorking": True,
            "updateTime": 1500
        }
    ]
    assert mapper.map_to_order_infos(json) == expected


def test_map_to_account_trade(mapper: BinanceModelsMapper) -> None:
    expected = BinanceAccountTradeModel(
        symbol="BTCUSDT",
        id=5,
        order_id=10,
        order_list_id=-1,
        price=Decimal("60000"),
        qty=Decimal("0.01"),
        quote_qty=Decimal("600"),
        commission=Decimal("0.00001"),
        commission_asset="BTC",
        time=1600,
        is_buyer=True,
        is_maker=False,
        is_best_match=True)
    json: BinanceAccountTradeJson = {
        "symbol": "BTCUSDT",
        "id": 5,
        "orderId": 10,
        "orderListId": -1,
        "price": "60000",
        "qty": "0.01",
        "quoteQty": "600",
        "commission": "0.00001",
        "commissionAsset": "BTC",
        "time": 1600,
        "isBuyer": True,
        "isMaker": False,
        "isBestMatch": True
    }

    assert mapper.map_to_account_trade(json) == expected


def test_map_to_account_trades(mapper: BinanceModelsMapper) -> None:
    expected = [
        BinanceAccountTradeModel(
            symbol="BTCUSDT",
            id=5,
            order_id=10,
            order_list_id=-1,
            price=Decimal("60000"),
            qty=Decimal("0.01"),
            quote_qty=Decimal("600"),
            commission=Decimal("0.00001"),
            commission_asset="BTC",
            time=1600,
            is_buyer=True,
            is_maker=False,
            is_best_match=True),
        BinanceAccountTradeModel(
            symbol="ETHUSDT",
            id=5,
            order_id=10,
            order_list_id=-1,
            price=Decimal("60000"),
            qty=Decimal("0.01"),
            quote_qty=Decimal("600"),
            commission=Decimal("0.00001"),
            commission_asset="BTC",
            time=1600,
            is_buyer=True,
            is_maker=False,
            is_best_match=True)
    ]
    json: BinanceAccountTradesJson = [
        {
            "symbol": "BTCUSDT",
            "id": 5,
            "orderId": 10,
            "orderListId": -1,
            "price": "60000",
            "qty": "0.01",
            "quoteQty": "600",
            "commission": "0.00001",
            "commissionAsset": "BTC",
            "time": 1600,
            "isBuyer": True,
            "isMaker": False,
            "isBestMatch": True
        },
        {
            "symbol": "ETHUSDT",
            "id": 5,
            "orderId": 10,
            "orderListId": -1,
            "price": "60000",
            "qty": "0.01",
            "quoteQty": "600",
            "commission": "0.00001",
            "commissionAsset": "BTC",
            "time": 1600,
            "isBuyer": True,
            "isMaker": False,
            "isBestMatch": True
        }
    ]

    assert mapper.map_to_account_trades(json) == expected
