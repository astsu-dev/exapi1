from decimal import Decimal
from typing import Final
from unittest import mock

import pytest
from exapi.response_handlers.binance.spot.trading import \
    BinanceSpotTradingResponseHandler
from exapi.enums.binance import (BinanceOrderSide, BinanceOrderStatus,
                                 BinanceOrderType, BinanceTimeInForce)
from exapi.models.binance import (BinanceAccountInfoModel,
                                  BinanceAccountTradeModel,
                                  BinanceCurrencyBalanceModel,
                                  BinanceFilledOrderModel,
                                  BinanceOrderInfoModel, BinanceOrderModel,
                                  BinanceTestOrderModel)
from exapi.models.binance.order import BinanceCanceledOrderModel

HANDLE_RESPONSE_PATH: Final[str] = "exapi.response_handlers.binance.spot.trading.handler.BinanceSpotTradingResponseHandler.handle_response"


@pytest.fixture(scope="module")
def handler() -> BinanceSpotTradingResponseHandler:
    return BinanceSpotTradingResponseHandler()


@pytest.mark.asyncio
async def test_handle_new_test_order_response(handler: BinanceSpotTradingResponseHandler) -> None:
    expected = BinanceTestOrderModel()
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {}
        assert await handler.handle_new_test_order_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_new_order_response(handler: BinanceSpotTradingResponseHandler) -> None:
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
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
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
        assert await handler.handle_new_order_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_cancel_order_response(handler: BinanceSpotTradingResponseHandler) -> None:
    expected = BinanceCanceledOrderModel(
        symbol="BTCUSDT",
        orig_client_order_id="sdf",
        order_id=5,
        order_list_id=-1,
        client_order_id="sdff",
        price=Decimal("100000.5"),
        orig_qty=Decimal("0.04"),
        executed_qty=Decimal("0.02"),
        cummulative_quote_qty=Decimal("4000"),
        status=BinanceOrderStatus.CANCELED,
        time_in_force=BinanceTimeInForce.GTC,
        type=BinanceOrderType.LIMIT,
        side=BinanceOrderSide.SELL)
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
        "symbol": "BTCUSDT",
        "origClientOrderId": "sdf",
        "orderId": 5,
        "orderListId": -1,
        "clientOrderId": "sdff",
        "price": "100000.5",
        "origQty": "0.04",
        "executedQty": "0.02",
        "cummulativeQuoteQty": "4000",
        "status": BinanceOrderStatus.CANCELED,
        "timeInForce": BinanceTimeInForce.GTC,
        "type": BinanceOrderType.LIMIT,
        "side": BinanceOrderSide.SELL
    }
        assert await handler.handle_cancel_order_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_cancel_orders_response(handler: BinanceSpotTradingResponseHandler) -> None:
    expected = [
        BinanceCanceledOrderModel(
            symbol="BTCUSDT",
            orig_client_order_id="sdf",
            order_id=5,
            order_list_id=-1,
            client_order_id="sdff",
            price=Decimal("100000.5"),
            orig_qty=Decimal("0.04"),
            executed_qty=Decimal("0.02"),
            cummulative_quote_qty=Decimal("4000"),
            status=BinanceOrderStatus.CANCELED,
            time_in_force=BinanceTimeInForce.GTC,
            type=BinanceOrderType.LIMIT,
            side=BinanceOrderSide.SELL),
        BinanceCanceledOrderModel(
            symbol="ETHUSDT",
            orig_client_order_id="sdf",
            order_id=5,
            order_list_id=-1,
            client_order_id="sdff",
            price=Decimal("100000.5"),
            orig_qty=Decimal("0.04"),
            executed_qty=Decimal("0.02"),
            cummulative_quote_qty=Decimal("4000"),
            status=BinanceOrderStatus.CANCELED,
            time_in_force=BinanceTimeInForce.GTC,
            type=BinanceOrderType.LIMIT,
            side=BinanceOrderSide.SELL)
    ]
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
        {
            "symbol": "BTCUSDT",
            "origClientOrderId": "sdf",
            "orderId": 5,
            "orderListId": -1,
            "clientOrderId": "sdff",
            "price": "100000.5",
            "origQty": "0.04",
            "executedQty": "0.02",
            "cummulativeQuoteQty": "4000",
            "status": BinanceOrderStatus.CANCELED,
            "timeInForce": BinanceTimeInForce.GTC,
            "type": BinanceOrderType.LIMIT,
            "side": BinanceOrderSide.SELL
        },
        {
            "symbol": "ETHUSDT",
            "origClientOrderId": "sdf",
            "orderId": 5,
            "orderListId": -1,
            "clientOrderId": "sdff",
            "price": "100000.5",
            "origQty": "0.04",
            "executedQty": "0.02",
            "cummulativeQuoteQty": "4000",
            "status": BinanceOrderStatus.CANCELED,
            "timeInForce": BinanceTimeInForce.GTC,
            "type": BinanceOrderType.LIMIT,
            "side": BinanceOrderSide.SELL
        }
    ]
        assert await handler.handle_cancel_orders_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_query_order_response(handler: BinanceSpotTradingResponseHandler) -> None:
    expected = BinanceOrderInfoModel(
        symbol="BTCUSDT",
        order_id=1234,
        order_list_id=1235,
        client_order_id="11cc",
        is_working=True,
        update_time=1500
    )
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
            "symbol": "BTCUSDT",
            "orderId": 1234,
            "orderListId": 1235,
            "clientOrderId": "11cc",
            "isWorking": True,
            "updateTime": 1500
        }
        assert await handler.handle_query_order_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_current_open_orders_response(handler: BinanceSpotTradingResponseHandler) -> None:
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
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
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
        assert await handler.handle_get_current_open_orders_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_all_orders_response(handler: BinanceSpotTradingResponseHandler) -> None:
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
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
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
        assert await handler.handle_get_all_orders_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_account_info_response(handler: BinanceSpotTradingResponseHandler) -> None:
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
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = {
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
        assert await handler.handle_get_account_info_response(mock.Mock()) == expected


@pytest.mark.asyncio
async def test_handle_get_trades_response(handler: BinanceSpotTradingResponseHandler) -> None:
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
    with mock.patch(HANDLE_RESPONSE_PATH) as handle_response:
        handle_response.return_value = [
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
        assert await handler.handle_get_trades_response(mock.Mock()) == expected
