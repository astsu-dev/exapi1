from decimal import Decimal
from typing import Final
from unittest import mock

import pytest
from exapi.response_handlers.hitbtc.market_data import HitbtcMarketDataResponseHandler
from exapi.models.hitbtc import (HitbtcCurrencyModel, HitbtcOrderBookModel,
                                 HitbtcOrderBookOrderModel, HitbtcSymbolModel,
                                 HitbtcTickerModel)

HANDLE_RESPONSE_PATH: Final[str] = "exapi.response_handlers.hitbtc.market_data.handler.HitbtcMarketDataResponseHandler.handle_response"


response_mock = mock.Mock()


@pytest.fixture(scope="module")
def handler() -> HitbtcMarketDataResponseHandler:
    return HitbtcMarketDataResponseHandler()


@pytest.mark.asyncio
async def test_handle_get_currencies_response(handler: HitbtcMarketDataResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
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
                "precisionPayout": 5,
                "precisionTransfer": 8
            }
        ]
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
        assert await handler.handle_get_currencies_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_get_certain_currency_response(handler: HitbtcMarketDataResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
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
        expected = HitbtcCurrencyModel(
            id="BTC", full_name="Bitcoin", crypto=True,
            payin_enabled=True, payin_payment_id=True,
            payin_confirmations=2, payout_enabled=False,
            payout_is_payment_id=True, transfer_enabled=True,
            delisted=False, payout_fee=Decimal("0.002"),
            precision_payout=5,
            precision_transfer=8
        )
        assert await handler.handle_get_certain_currency_response(
            response_mock) == expected


@pytest.mark.asyncio
async def test_handle_get_symbols_response(handler: HitbtcMarketDataResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
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
        assert await handler.handle_get_symbols_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_get_certain_symbol_response(handler: HitbtcMarketDataResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "id": "ETHBTC",
            "baseCurrency": "ETH",
            "quoteCurrency": "BTC",
            "quantityIncrement": "0.000001",
            "tickSize": "0.001",
            "takeLiquidityRate": "0.01",
            "provideLiquidityRate": "0.01",
            "feeCurrency": "BTC"
        }
        expected = HitbtcSymbolModel(
            id="ETHBTC",
            base_currency="ETH",
            quote_currency="BTC",
            quantity_increment=Decimal("0.000001"),
            tick_size=Decimal("0.001"),
            take_liquidity_rate=Decimal("0.01"),
            provide_liquidity_rate=Decimal("0.01"),
            fee_currency="BTC")
        assert await handler.handle_get_certain_symbol_response(
            response_mock) == expected


@pytest.mark.asyncio
async def test_handle_get_order_books_response(handler: HitbtcMarketDataResponseHandler) -> None:
    ask_orders = [
        HitbtcOrderBookOrderModel(
            price=Decimal("0.001"), size=Decimal("10.5")),
        HitbtcOrderBookOrderModel(price=Decimal("0.002"), size=Decimal("12.5"))]
    bid_orders = [
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
    raw_ask_orders = [
        {
            "price": "0.001",
            "size": "10.5"
        }, {
            "price": "0.002",
            "size": "12.5"
        }]
    raw_bid_orders = [
        {
            "price": "0.0005",
            "size": "10.5"
        }, {
            "price": "0.0004",
            "size": "12.5"
        }]
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
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
        assert await handler.handle_get_order_books_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_get_certain_order_book_response(handler: HitbtcMarketDataResponseHandler) -> None:
    ask_orders = [
        HitbtcOrderBookOrderModel(
            price=Decimal("0.001"), size=Decimal("10.5")),
        HitbtcOrderBookOrderModel(price=Decimal("0.002"), size=Decimal("12.5"))]
    bid_orders = [
        HitbtcOrderBookOrderModel(price=Decimal(
            "0.0005"), size=Decimal("10.5")),
        HitbtcOrderBookOrderModel(price=Decimal("0.0004"), size=Decimal("12.5"))]

    expected = HitbtcOrderBookModel(
        ask=ask_orders,
        bid=bid_orders,
        timestamp="1234",
        symbol="BTCUSDT")

    raw_ask_orders = [
        {
            "price": "0.001",
            "size": "10.5"
        }, {
            "price": "0.002",
            "size": "12.5"
        }]
    raw_bid_orders = [
        {
            "price": "0.0005",
            "size": "10.5"
        }, {
            "price": "0.0004",
            "size": "12.5"
        }]
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "ask": raw_ask_orders,
            "bid": raw_bid_orders,
            "timestamp": "1234",
            "symbol": "BTCUSDT"
        }
        assert await handler.handle_get_certain_order_book_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_get_certain_ticker_response(handler: HitbtcMarketDataResponseHandler) -> None:
    expected = HitbtcTickerModel(
        symbol="BTCUSDT",
        low=Decimal("0.002"),
        high=Decimal("0.004"),
        volume=Decimal("1800.4"),
        volume_quote=Decimal("50055.3"),
        timestamp="1234")
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
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

        assert await handler.handle_get_certain_ticker_response(response_mock) == expected
