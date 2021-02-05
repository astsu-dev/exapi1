from decimal import Decimal
from typing import Final
from unittest import mock

import pytest
from exapi.api.hitbtc.trading import HitbtcTradingResponseHandler
from exapi.models.hitbtc import (HitbtcOrderModel,
                                 HitbtcTradingCurrencyBalanceModel,
                                 HitbtcTradingFeeModel)

HANDLE_RESPONSE_PATH: Final[str] = "exapi.api.hitbtc.trading.response_handler.handler.HitbtcTradingResponseHandler.handle_response"


response_mock = mock.Mock()


@pytest.fixture(scope="module")
def handler() -> HitbtcTradingResponseHandler:
    return HitbtcTradingResponseHandler()


@pytest.mark.asyncio
async def test_handle_get_trading_balance_response(handler: HitbtcTradingResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
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
        assert await handler.handle_get_trading_balance_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_get_active_order_response(handler: HitbtcTradingResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
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
        assert await handler.handle_get_active_order_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_get_active_orders_response(handler: HitbtcTradingResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
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
        assert await handler.handle_get_active_orders_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_new_order_response(handler: HitbtcTradingResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
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
        assert await handler.handle_new_order_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_cancel_orders_response(handler: HitbtcTradingResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
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
        assert await handler.handle_cancel_orders_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_cancel_order_response(handler: HitbtcTradingResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
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
        assert await handler.handle_cancel_order_response(response_mock) == expected


@pytest.mark.asyncio
async def test_handle_get_fee_response(handler: HitbtcTradingResponseHandler) -> None:
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "takeLiquidityRate": "0.0001",
            "provideLiquidityRate": "0.0002"
        }
        expected = HitbtcTradingFeeModel(
            take_liquidity_rate=Decimal("0.0001"),
            provide_liquidity_rate=Decimal("0.0002"))
        assert await handler.handle_get_fee_response(response_mock) == expected
