from decimal import Decimal
from typing import List

import pytest
from exapi.models.hitbtc import (HitbtcCandleModel, HitbtcCurrencyModel,
                                 HitbtcOrderBookModel,
                                 HitbtcOrderBookOrderModel, HitbtcOrderModel,
                                 HitbtcRawCandleModel, HitbtcRawCurrencies,
                                 HitbtcRawCurrencyModel,
                                 HitbtcRawOrderBookModel,
                                 HitbtcRawOrderBookOrderModel,
                                 HitbtcRawOrderBooks, HitbtcRawOrderModel,
                                 HitbtcRawSymbolCandles, HitbtcRawSymbolModel,
                                 HitbtcRawSymbols, HitbtcRawSymbolTrades,
                                 HitbtcRawTickerModel, HitbtcRawTickers,
                                 HitbtcRawTradeModel, HitbtcRawTrades,
                                 HitbtcRawTradingCurrencyBalanceModel,
                                 HitbtcRawTradingCurrencyBalances,
                                 HitbtcRawTradingFeeModel, HitbtcSymbolModel,
                                 HitbtcTickerModel, HitbtcTradeModel,
                                 HitbtcTradingCurrencyBalanceModel,
                                 HitbtcTradingFeeModel)
from exapi.models.hitbtc.mapper import HitbtcModelsMapper
from exapi.models.hitbtc.order import HitbtcRawOrders


@pytest.fixture(scope="module")
def mapper() -> HitbtcModelsMapper:
    return HitbtcModelsMapper()


def test_map_to_currency(mapper: HitbtcModelsMapper) -> None:
    expected = HitbtcCurrencyModel(
        id="BTC", full_name="Bitcoin", crypto=True,
        payin_enabled=True, payin_payment_id=True,
        payin_confirmations=2, payout_enabled=False,
        payout_is_payment_id=True, transfer_enabled=True,
        delisted=False, payout_fee=Decimal("0.002"),
        precision_payout=5,
        precision_transfer=8
    )
    raw: HitbtcRawCurrencyModel = {
        "id": "BTC",
        "fullName": "Bitcoin",
        "crypto": True,
        "payinEnabled": True,
        "payinPaymentId": True,
        "payinConfirmations": 2,
        "payoutEnabled": False,
        "payoutIsPaymentId": True,
        "transferEnabled": True,
        "delisted": False,
        "payoutFee": "0.002",
        "precisionPayout": 5,
        "precisionTransfer": 8
    }
    assert mapper.map_to_currency(raw) == expected


def test_map_to_currencies(mapper: HitbtcModelsMapper) -> None:
    expected = [
        HitbtcCurrencyModel(
            id="BTC", full_name="Bitcoin", crypto=True,
            payin_enabled=True, payin_payment_id=True,
            payin_confirmations=2, payout_enabled=False,
            payout_is_payment_id=True, transfer_enabled=True,
            delisted=False, payout_fee=Decimal("0.002"),
            precision_payout=5,
            precision_transfer=8
        ),
        HitbtcCurrencyModel(
            id="ETH", full_name="Ethereum", crypto=True,
            payin_enabled=True, payin_payment_id=True,
            payin_confirmations=2, payout_enabled=False,
            payout_is_payment_id=True, transfer_enabled=True,
            delisted=False, payout_fee=Decimal("0.003"),
            precision_payout=5,
            precision_transfer=8
        )
    ]
    raw: HitbtcRawCurrencies = [
        {
            "id": "BTC",
            "fullName": "Bitcoin",
            "crypto": True,
            "payinEnabled": True,
            "payinPaymentId": True,
            "payinConfirmations": 2,
            "payoutEnabled": False,
            "payoutIsPaymentId": True,
            "transferEnabled": True,
            "delisted": False,
            "payoutFee": "0.002",
            "payoutMinimalAmount": "0.001",
            "precisionPayout": 5,
            "precisionTransfer": 8
        },
        {
            "id": "ETH",
            "fullName": "Ethereum",
            "crypto": True,
            "payinEnabled": True,
            "payinPaymentId": True,
            "payinConfirmations": 2,
            "payoutEnabled": False,
            "payoutIsPaymentId": True,
            "transferEnabled": True,
            "delisted": False,
            "payoutFee": "0.003",
            "payoutMinimalAmount": "0.001",
            "precisionPayout": 5,
            "precisionTransfer": 8
        }
    ]
    assert mapper.map_to_currencies(raw) == expected


def test_map_to_symbol(mapper: HitbtcModelsMapper) -> None:
    expected = HitbtcSymbolModel(
        id="ETHBTC",
        base_currency="ETH",
        quote_currency="BTC",
        quantity_increment=Decimal("0.000001"),
        tick_size=Decimal("0.001"),
        take_liquidity_rate=Decimal("0.01"),
        provide_liquidity_rate=Decimal("0.01"),
        fee_currency="BTC")
    raw: HitbtcRawSymbolModel = {
        "id": "ETHBTC",
        "baseCurrency": "ETH",
        "quoteCurrency": "BTC",
        "quantityIncrement": "0.000001",
        "tickSize": "0.001",
        "takeLiquidityRate": "0.01",
        "provideLiquidityRate": "0.01",
        "feeCurrency": "BTC"
    }
    assert mapper.map_to_symbol(raw) == expected


def test_map_to_symbols(mapper: HitbtcModelsMapper) -> None:
    expected = [
        HitbtcSymbolModel(
            id="ETHBTC",
            base_currency="ETH",
            quote_currency="BTC",
            quantity_increment=Decimal("0.000001"),
            tick_size=Decimal("0.001"),
            take_liquidity_rate=Decimal("0.01"),
            provide_liquidity_rate=Decimal("0.01"),
            fee_currency="BTC"),
        HitbtcSymbolModel(
            id="LTCBTC",
            base_currency="LTC",
            quote_currency="BTC",
            quantity_increment=Decimal("0.000001"),
            tick_size=Decimal("0.002"),
            take_liquidity_rate=Decimal("0.01"),
            provide_liquidity_rate=Decimal("0.01"),
            fee_currency="BTC")
    ]
    raw: HitbtcRawSymbols = [
        {
            "id": "ETHBTC",
            "baseCurrency": "ETH",
            "quoteCurrency": "BTC",
            "quantityIncrement": "0.000001",
            "tickSize": "0.001",
            "takeLiquidityRate": "0.01",
            "provideLiquidityRate": "0.01",
            "feeCurrency": "BTC"
        },
        {
            "id": "LTCBTC",
            "baseCurrency": "LTC",
            "quoteCurrency": "BTC",
            "quantityIncrement": "0.000001",
            "tickSize": "0.002",
            "takeLiquidityRate": "0.01",
            "provideLiquidityRate": "0.01",
            "feeCurrency": "BTC"
        }
    ]
    assert mapper.map_to_symbols(raw) == expected


def test_map_to_orderbook_order(mapper: HitbtcModelsMapper) -> None:
    expected = HitbtcOrderBookOrderModel(
        price=Decimal("0.001"), size=Decimal("10.5"))
    raw: HitbtcRawOrderBookOrderModel = {
        "price": "0.001",
        "size": "10.5"
    }
    assert mapper.map_to_orderbook_order(raw) == expected


def test_map_to_orderbook(mapper: HitbtcModelsMapper) -> None:
    raw_ask_orders: List[HitbtcRawOrderBookOrderModel] = [
        {
            "price": "0.001",
            "size": "10.5"
        }, {
            "price": "0.002",
            "size": "12.5"
        }]
    raw_bid_orders: List[HitbtcRawOrderBookOrderModel] = [
        {
            "price": "0.0005",
            "size": "10.5"
        }, {
            "price": "0.0004",
            "size": "12.5"
        }]

    ask_orders: List[HitbtcOrderBookOrderModel] = [
        HitbtcOrderBookOrderModel(
            price=Decimal("0.001"), size=Decimal("10.5")),
        HitbtcOrderBookOrderModel(price=Decimal("0.002"), size=Decimal("12.5"))]
    bid_orders: List[HitbtcOrderBookOrderModel] = [
        HitbtcOrderBookOrderModel(price=Decimal(
            "0.0005"), size=Decimal("10.5")),
        HitbtcOrderBookOrderModel(price=Decimal("0.0004"), size=Decimal("12.5"))]

    expected = HitbtcOrderBookModel(
        ask=ask_orders,
        bid=bid_orders,
        timestamp="1234",
        symbol="BTCUSDT")
    raw: HitbtcRawOrderBookModel = {
        "ask": raw_ask_orders,
        "bid": raw_bid_orders,
        "timestamp": "1234",
        "symbol": "BTCUSDT"
    }
    assert mapper.map_to_orderbook(raw) == expected


def test_map_to_orderbooks(mapper: HitbtcModelsMapper) -> None:
    raw_ask_orders: List[HitbtcRawOrderBookOrderModel] = [
        {
            "price": "0.001",
            "size": "10.5"
        }, {
            "price": "0.002",
            "size": "12.5"
        }]
    raw_bid_orders: List[HitbtcRawOrderBookOrderModel] = [
        {
            "price": "0.0005",
            "size": "10.5"
        }, {
            "price": "0.0004",
            "size": "12.5"
        }]

    ask_orders: List[HitbtcOrderBookOrderModel] = [
        HitbtcOrderBookOrderModel(
            price=Decimal("0.001"), size=Decimal("10.5")),
        HitbtcOrderBookOrderModel(price=Decimal("0.002"), size=Decimal("12.5"))]
    bid_orders: List[HitbtcOrderBookOrderModel] = [
        HitbtcOrderBookOrderModel(price=Decimal(
            "0.0005"), size=Decimal("10.5")),
        HitbtcOrderBookOrderModel(price=Decimal("0.0004"), size=Decimal("12.5"))]

    expected = {
        "BTCUSDT": HitbtcOrderBookModel(
            ask=ask_orders,
            bid=bid_orders,
            timestamp="1234",
            symbol="BTCUSDT"),
        "ETHUSDT": HitbtcOrderBookModel(
            ask=ask_orders,
            bid=bid_orders,
            timestamp="1235",
            symbol="ETHUSDT")
    }
    raw: HitbtcRawOrderBooks = {
        "BTCUSDT": {
            "ask": raw_ask_orders,
            "bid": raw_bid_orders,
            "timestamp": "1234",
            "symbol": "BTCUSDT"
        },
        "ETHUSDT": {
            "ask": raw_ask_orders,
            "bid": raw_bid_orders,
            "timestamp": "1235",
            "symbol": "ETHUSDT"
        }
    }

    assert mapper.map_to_orderbooks(raw) == expected


def test_map_to_ticker(mapper: HitbtcModelsMapper) -> None:
    expected = HitbtcTickerModel(
        symbol="BTCUSDT",
        low=Decimal("0.002"),
        high=Decimal("0.004"),
        volume=Decimal("1800.4"),
        volume_quote=Decimal("50055.3"),
        timestamp="1234")
    raw: HitbtcRawTickerModel = {
        "symbol": "BTCUSDT",
        "low": "0.002",
        "high": "0.004",
        "volume": "1800.4",
        "volumeQuote": "50055.3",
        "timestamp": "1234",
        "ask": None,
        "bid": None,
        "last": None,
        "open": None
    }
    assert mapper.map_to_ticker(raw) == expected

    expected = HitbtcTickerModel(
        symbol="BTCUSDT",
        low=Decimal("0.002"),
        high=Decimal("0.004"),
        volume=Decimal("1800.4"),
        volume_quote=Decimal("50055.3"),
        timestamp="1234",
        ask=Decimal("15.5"),
        bid=Decimal("4.5"),
        last=Decimal("3.5"),
        open=Decimal("6.5"))
    raw = {
        "symbol": "BTCUSDT",
        "low": "0.002",
        "high": "0.004",
        "volume": "1800.4",
        "volumeQuote": "50055.3",
        "timestamp": "1234",
        "ask": "15.5",
        "bid": "4.5",
        "last": "3.5",
        "open": "6.5"
    }
    assert mapper.map_to_ticker(raw) == expected


def test_map_to_tickers(mapper: HitbtcModelsMapper) -> None:
    expected = [
        HitbtcTickerModel(
            symbol="BTCUSDT",
            low=Decimal("0.002"),
            high=Decimal("0.004"),
            volume=Decimal("1800.4"),
            volume_quote=Decimal("50055.3"),
            timestamp="1234"),
        HitbtcTickerModel(
            symbol="ETHUSDT",
            low=Decimal("0.003"),
            high=Decimal("0.005"),
            volume=Decimal("1800.4"),
            volume_quote=Decimal("50055.3"),
            timestamp="1234")
    ]
    raw: HitbtcRawTickers = [
        {
            "symbol": "BTCUSDT",
            "low": "0.002",
            "high": "0.004",
            "volume": "1800.4",
            "volumeQuote": "50055.3",
            "timestamp": "1234",
            "ask": None,
            "bid": None,
            "last": None,
            "open": None
        },
        {
            "symbol": "ETHUSDT",
            "low": "0.003",
            "high": "0.005",
            "volume": "1800.4",
            "volumeQuote": "50055.3",
            "timestamp": "1234",
            "ask": None,
            "bid": None,
            "last": None,
            "open": None
        }]
    assert mapper.map_to_tickers(raw) == expected


def test_map_to_trade(mapper: HitbtcModelsMapper) -> None:
    expected = HitbtcTradeModel(
        id=45,
        price=Decimal("456.6"),
        quantity=Decimal("234"),
        side="sell",
        timestamp="1234")
    raw: HitbtcRawTradeModel = {
        "id": 45,
        "price": "456.6",
        "quantity": "234",
        "side": "sell",
        "timestamp": "1234"
    }
    assert mapper.map_to_trade(raw) == expected


def test_map_to_symbol_trades(mapper: HitbtcModelsMapper) -> None:
    expected = [
        HitbtcTradeModel(
            id=45,
            price=Decimal("456.6"),
            quantity=Decimal("234"),
            side="sell",
            timestamp="1234"),
        HitbtcTradeModel(
            id=46,
            price=Decimal("456.6"),
            quantity=Decimal("234"),
            side="buy",
            timestamp="1235")
    ]
    raw: HitbtcRawSymbolTrades = [
        {
            "id": 45,
            "price": "456.6",
            "quantity": "234",
            "side": "sell",
            "timestamp": "1234"
        },
        {
            "id": 46,
            "price": "456.6",
            "quantity": "234",
            "side": "buy",
            "timestamp": "1235"
        }
    ]
    assert mapper.map_to_symbol_trades(raw) == expected


def test_map_to_trades(mapper: HitbtcModelsMapper) -> None:
    raw_symbol_trades: HitbtcRawSymbolTrades = [
        {
            "id": 45,
            "price": "456.6",
            "quantity": "234",
            "side": "sell",
            "timestamp": "1234"
        },
        {
            "id": 46,
            "price": "456.6",
            "quantity": "234",
            "side": "buy",
            "timestamp": "1235"
        }
    ]

    symbol_trades = [
        HitbtcTradeModel(
            id=45,
            price=Decimal("456.6"),
            quantity=Decimal("234"),
            side="sell",
            timestamp="1234"),
        HitbtcTradeModel(
            id=46,
            price=Decimal("456.6"),
            quantity=Decimal("234"),
            side="buy",
            timestamp="1235")
    ]

    expected = {
        "BTCUSDT": symbol_trades,
        "ETHUSDT": symbol_trades
    }

    raw: HitbtcRawTrades = {
        "BTCUSDT": raw_symbol_trades,
        "ETHUSDT": raw_symbol_trades
    }
    assert mapper.map_to_trades(raw) == expected


def test_map_to_candle(mapper: HitbtcModelsMapper) -> None:
    expected = HitbtcCandleModel(
        timestamp="1234",
        open=Decimal("15.5"),
        close=Decimal("17.4"),
        min=Decimal("12.5"),
        max=Decimal("17.4"),
        volume=Decimal("177.9"),
        volume_quote=Decimal("188.2"))

    raw: HitbtcRawCandleModel = {
        "timestamp": "1234",
        "open": "15.5",
        "close": "17.4",
        "min": "12.5",
        "max": "17.4",
        "volume": "177.9",
        "volumeQuote": "188.2"
    }

    assert mapper.map_to_candle(raw) == expected


def test_map_to_symbol_candles(mapper: HitbtcModelsMapper) -> None:
    expected = [
        HitbtcCandleModel(
            timestamp="1234",
            open=Decimal("15.5"),
            close=Decimal("17.4"),
            min=Decimal("12.5"),
            max=Decimal("17.4"),
            volume=Decimal("177.9"),
            volume_quote=Decimal("188.2")),
        HitbtcCandleModel(
            timestamp="1235",
            open=Decimal("25.5"),
            close=Decimal("17.4"),
            min=Decimal("12.5"),
            max=Decimal("17.4"),
            volume=Decimal("177.9"),
            volume_quote=Decimal("188.2"))
    ]

    raw: HitbtcRawSymbolCandles = [
        {
            "timestamp": "1234",
            "open": "15.5",
            "close": "17.4",
            "min": "12.5",
            "max": "17.4",
            "volume": "177.9",
            "volumeQuote": "188.2"
        },
        {
            "timestamp": "1235",
            "open": "25.5",
            "close": "17.4",
            "min": "12.5",
            "max": "17.4",
            "volume": "177.9",
            "volumeQuote": "188.2"
        }
    ]

    assert mapper.map_to_symbol_candles(raw) == expected


def test_map_to_candles(mapper: HitbtcModelsMapper) -> None:
    raw_symbol_candles: HitbtcRawSymbolCandles = [
        {
            "timestamp": "1234",
            "open": "15.5",
            "close": "17.4",
            "min": "12.5",
            "max": "17.4",
            "volume": "177.9",
            "volumeQuote": "188.2"
        },
        {
            "timestamp": "1235",
            "open": "25.5",
            "close": "17.4",
            "min": "12.5",
            "max": "17.4",
            "volume": "177.9",
            "volumeQuote": "188.2"
        }
    ]
    symbol_candles = [
        HitbtcCandleModel(
            timestamp="1234",
            open=Decimal("15.5"),
            close=Decimal("17.4"),
            min=Decimal("12.5"),
            max=Decimal("17.4"),
            volume=Decimal("177.9"),
            volume_quote=Decimal("188.2")),
        HitbtcCandleModel(
            timestamp="1235",
            open=Decimal("25.5"),
            close=Decimal("17.4"),
            min=Decimal("12.5"),
            max=Decimal("17.4"),
            volume=Decimal("177.9"),
            volume_quote=Decimal("188.2"))
    ]

    expected = {
        "BTCUSDT": symbol_candles,
        "ETHUSDT": symbol_candles
    }
    raw = {
        "BTCUSDT": raw_symbol_candles,
        "ETHUSDT": raw_symbol_candles
    }

    assert mapper.map_to_candles(raw) == expected


def test_map_to_order(mapper: HitbtcModelsMapper) -> None:
    expected = HitbtcOrderModel(
        id=5,
        client_order_id="234j3k242",
        symbol="BTCUSDT",
        side="sell",
        status="new",
        type="limit",
        time_in_force="GTC",
        quantity=Decimal("0.001"),
        price=Decimal("0.002"),
        cum_quantity=Decimal("1.3"),
        created_at="1234",
        updated_at="1234",
        post_only=True,
        avg_price=Decimal("0.56"),
        stop_price=Decimal("0.12"),
        expire_time="1234")
    raw: HitbtcRawOrderModel = {
        "id": 5,
        "clientOrderId": "234j3k242",
        "symbol": "BTCUSDT",
        "side": "sell",
        "status": "new",
        "type": "limit",
        "timeInForce": "GTC",
        "quantity": "0.001",
        "price": "0.002",
        "cumQuantity": "1.3",
        "createdAt": "1234",
        "updatedAt": "1234",
        "postOnly": True,
        "avgPrice": "0.56",
        "stopPrice": "0.12",
        "expireTime": "1234"
    }

    assert mapper.map_to_order(raw) == expected

    expected = HitbtcOrderModel(
        id=5,
        client_order_id="234j3k242",
        symbol="BTCUSDT",
        side="sell",
        status="new",
        type="limit",
        time_in_force="GTC",
        quantity=Decimal("0.001"),
        price=Decimal("0.002"),
        cum_quantity=Decimal("1.3"),
        created_at="1234",
        updated_at="1234",
        post_only=True,
        avg_price=Decimal("0.56"),
        stop_price=Decimal("0.12"),
        expire_time="1234",
        trades_report=[
            HitbtcTradeModel(
                id=45,
                price=Decimal("456.6"),
                quantity=Decimal("234"),
                side="sell",
                timestamp="1234"),
            HitbtcTradeModel(
                id=46,
                price=Decimal("456.6"),
                quantity=Decimal("234"),
                side="buy",
                timestamp="1235")
        ])
    raw = {
        "id": 5,
        "clientOrderId": "234j3k242",
        "symbol": "BTCUSDT",
        "side": "sell",
        "status": "new",
        "type": "limit",
        "timeInForce": "GTC",
        "quantity": "0.001",
        "price": "0.002",
        "cumQuantity": "1.3",
        "createdAt": "1234",
        "updatedAt": "1234",
        "postOnly": True,
        "avgPrice": "0.56",
        "stopPrice": "0.12",
        "expireTime": "1234",
        "tradesReport": [
            {
                "id": 45,
                "price": "456.6",
                "quantity": "234",
                "side": "sell",
                "timestamp": "1234"
            },
            {
                "id": 46,
                "price": "456.6",
                "quantity": "234",
                "side": "buy",
                "timestamp": "1235"
            }
        ]
    }

    assert mapper.map_to_order(raw) == expected


def test_map_to_orders(mapper: HitbtcModelsMapper) -> None:
    expected = [
        HitbtcOrderModel(
            id=5,
            client_order_id="234j3k242",
            symbol="BTCUSDT",
            side="sell",
            status="new",
            type="limit",
            time_in_force="GTC",
            quantity=Decimal("0.001"),
            price=Decimal("0.002"),
            cum_quantity=Decimal("1.3"),
            created_at="1234",
            updated_at="1234",
            post_only=True,
            avg_price=Decimal("0.56"),
            stop_price=Decimal("0.12"),
            expire_time="1234"),
        HitbtcOrderModel(
            id=5,
            client_order_id="234j3k242",
            symbol="BTCUSDT",
            side="sell",
            status="new",
            type="limit",
            time_in_force="GTC",
            quantity=Decimal("0.001"),
            price=Decimal("0.002"),
            cum_quantity=Decimal("1.3"),
            created_at="1234",
            updated_at="1234",
            post_only=True,
            avg_price=Decimal("0.56"),
            stop_price=Decimal("0.12"),
            expire_time="1234")
    ]
    raw: HitbtcRawOrders = [{
        "id": 5,
        "clientOrderId": "234j3k242",
        "symbol": "BTCUSDT",
        "side": "sell",
        "status": "new",
        "type": "limit",
        "timeInForce": "GTC",
        "quantity": "0.001",
        "price": "0.002",
        "cumQuantity": "1.3",
        "createdAt": "1234",
        "updatedAt": "1234",
        "postOnly": True,
        "avgPrice": "0.56",
        "stopPrice": "0.12",
        "expireTime": "1234"
    },
        {
        "id": 5,
        "clientOrderId": "234j3k242",
        "symbol": "BTCUSDT",
        "side": "sell",
        "status": "new",
        "type": "limit",
        "timeInForce": "GTC",
        "quantity": "0.001",
        "price": "0.002",
        "cumQuantity": "1.3",
        "createdAt": "1234",
        "updatedAt": "1234",
        "postOnly": True,
        "avgPrice": "0.56",
        "stopPrice": "0.12",
        "expireTime": "1234"
    }
    ]

    assert mapper.map_to_orders(raw) == expected

    expected = [
        HitbtcOrderModel(
            id=5,
            client_order_id="234j3k242",
            symbol="BTCUSDT",
            side="sell",
            status="new",
            type="limit",
            time_in_force="GTC",
            quantity=Decimal("0.001"),
            price=Decimal("0.002"),
            cum_quantity=Decimal("1.3"),
            created_at="1234",
            updated_at="1234",
            post_only=True,
            avg_price=Decimal("0.56"),
            stop_price=Decimal("0.12"),
            expire_time="1234",
            trades_report=[
                HitbtcTradeModel(
                    id=45,
                    price=Decimal("456.6"),
                    quantity=Decimal("234"),
                    side="sell",
                    timestamp="1234"),
                HitbtcTradeModel(
                    id=46,
                    price=Decimal("456.6"),
                    quantity=Decimal("234"),
                    side="buy",
                    timestamp="1235")
            ]),
        HitbtcOrderModel(
            id=5,
            client_order_id="234j3k242",
            symbol="BTCUSDT",
            side="sell",
            status="new",
            type="limit",
            time_in_force="GTC",
            quantity=Decimal("0.001"),
            price=Decimal("0.002"),
            cum_quantity=Decimal("1.3"),
            created_at="1234",
            updated_at="1234",
            post_only=True,
            avg_price=Decimal("0.56"),
            stop_price=Decimal("0.12"),
            expire_time="1234",
            trades_report=[
                HitbtcTradeModel(
                    id=45,
                    price=Decimal("456.6"),
                    quantity=Decimal("234"),
                    side="sell",
                    timestamp="1234"),
                HitbtcTradeModel(
                    id=46,
                    price=Decimal("456.6"),
                    quantity=Decimal("234"),
                    side="buy",
                    timestamp="1235")
            ])]
    raw = [
        {
            "id": 5,
            "clientOrderId": "234j3k242",
            "symbol": "BTCUSDT",
            "side": "sell",
            "status": "new",
            "type": "limit",
            "timeInForce": "GTC",
            "quantity": "0.001",
            "price": "0.002",
            "cumQuantity": "1.3",
            "createdAt": "1234",
            "updatedAt": "1234",
            "postOnly": True,
            "avgPrice": "0.56",
            "stopPrice": "0.12",
            "expireTime": "1234",
            "tradesReport": [
                {
                    "id": 45,
                    "price": "456.6",
                    "quantity": "234",
                    "side": "sell",
                    "timestamp": "1234"
                },
                {
                    "id": 46,
                    "price": "456.6",
                    "quantity": "234",
                    "side": "buy",
                    "timestamp": "1235"
                }
            ]
        },
        {
            "id": 5,
            "clientOrderId": "234j3k242",
            "symbol": "BTCUSDT",
            "side": "sell",
            "status": "new",
            "type": "limit",
            "timeInForce": "GTC",
            "quantity": "0.001",
            "price": "0.002",
            "cumQuantity": "1.3",
            "createdAt": "1234",
            "updatedAt": "1234",
            "postOnly": True,
            "avgPrice": "0.56",
            "stopPrice": "0.12",
            "expireTime": "1234",
            "tradesReport": [
                {
                    "id": 45,
                    "price": "456.6",
                    "quantity": "234",
                    "side": "sell",
                    "timestamp": "1234"
                },
                {
                    "id": 46,
                    "price": "456.6",
                    "quantity": "234",
                    "side": "buy",
                    "timestamp": "1235"
                }
            ]
        }
    ]

    assert mapper.map_to_orders(raw) == expected


def test_map_to_trading_currency_balance(mapper: HitbtcModelsMapper) -> None:
    expected = HitbtcTradingCurrencyBalanceModel(
        currency="BTCUSDT",
        available=Decimal("0.1"),
        reserved=Decimal("0.05"))
    raw: HitbtcRawTradingCurrencyBalanceModel = {
        "currency": "BTCUSDT",
        "available": "0.1",
        "reserved": "0.05"
    }
    assert mapper.map_to_trading_currency_balance(raw) == expected


def test_map_to_trading_balance(mapper: HitbtcModelsMapper) -> None:
    expected = [
        HitbtcTradingCurrencyBalanceModel(
            currency="BTCUSDT",
            available=Decimal("0.1"),
            reserved=Decimal("0.05")),
        HitbtcTradingCurrencyBalanceModel(
            currency="ETHUSDT",
            available=Decimal("0.3"),
            reserved=Decimal("0.07"))
    ]
    raw: HitbtcRawTradingCurrencyBalances = [
        {
            "currency": "BTCUSDT",
            "available": "0.1",
            "reserved": "0.05"
        },
        {
            "currency": "ETHUSDT",
            "available": "0.3",
            "reserved": "0.07"
        }
    ]
    assert mapper.map_to_trading_balance(raw) == expected


def test_map_to_trading_fee(mapper: HitbtcModelsMapper) -> None:
    expected = HitbtcTradingFeeModel(
        take_liquidity_rate=Decimal("0.0001"),
        provide_liquidity_rate=Decimal("0.0002"))
    raw: HitbtcRawTradingFeeModel = {
        "takeLiquidityRate": "0.0001",
        "provideLiquidityRate": "0.0002"
    }
    assert mapper.map_to_trading_fee(raw) == expected
