from typing import Optional

from exapi.models.hitbtc.typedefs import (Datetime, OrderSide, OrderType,
                                          Symbol, TimeInForce)
from exapi.requesters.base import BaseRequester
from exapi.requesters.typedefs import RequesterResponse, Session

from .interface import IHitbtcTradingRequester
from .request_creator import IHitbtcTradingRequestCreator


class HitbtcTradingRequester(BaseRequester, IHitbtcTradingRequester):
    """Has methods for hitbtc trading requests making."""

    def __init__(self, session: Session,
                 creator: IHitbtcTradingRequestCreator
                 ) -> None:
        """Class initialization.

        Args:
            session (Optional[session], optional): aiohttp session. Defaults to None.
            creator (Optional[IHitbtcTradingRequestCreator], optional): request creator.
                Defaults to None.
        """

        self._session = session
        self._creator = creator

    async def get_trading_balance(self) -> RequesterResponse:
        """Returns a response with the user's trading balance.

        Requires the "Orderbook, History, Trading balance" API key Access Right.

        Returns:
            RequesterResponse
        """

        req = self._creator.create_get_trading_balance_request()
        res = await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)
        return res

    async def get_active_orders(self, symbol: Optional[Symbol] = None) -> RequesterResponse:
        """Return a response with array of active orders.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            symbol (Optional[Symbol])

        Returns:
            RequesterResponse
        """

        req = self._creator.create_get_active_orders_request(
            symbol=symbol)
        res = await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)
        return res

    async def get_active_order(self, client_order_id: str,
                               wait: Optional[int] = None
                               ) -> RequesterResponse:
        """Returns a response with the order by `client_order_id`.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            client_order_id (str)
            wait (Optional[int], optional): Time in milliseconds.
                Max value: 60000. Default value: none.
                While using long polling request: if order is filled,
                cancelled or expired order info will be returned instantly.
                For other order statuses, actual order info
                will be returned after specified wait time.

        Returns:
            RequesterResponse
        """

        req = self._creator.create_get_active_order_request(
            client_order_id=client_order_id, wait=wait)
        res = await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)
        return res

    async def new_order(self, symbol: Symbol,
                        side: OrderSide,
                        quantity: str,
                        price: str,
                        type_: Optional[OrderType] = None,
                        time_in_force: Optional[TimeInForce] = None,
                        stop_price: Optional[str] = None,
                        expire_time: Optional[Datetime] = None,
                        strict_validate: Optional[bool] = None,
                        post_only: Optional[bool] = None,
                        client_order_id: Optional[str] = None,
                        ) -> RequesterResponse:
        """Requires the "Place/cancel orders" API key Accekss Right.

        Price accuracy and quantity

        Symbol config contains the tickSize parameter
        which means that price should be divided by tickSize with no remainder.
        quantity should be divided by quantityIncrement with no remainder.
        By default, if strict_validate is not enabled,
        the Server rounds half down the price and quantity for tickSize and quantityIncrement.

        Example of ETHBTC: tickSize = '0.000001',
        then price '0.046016' is valid, '0.0460165' is invalid.

        Fees

        Charged fee is determined in symbol's feeCurrency.
        Maker-taker fees offer a transaction rebate provideLiquidityRate
        to those who provide liquidity (the market maker),
        while charging customers who take that liquidity takeLiquidityRate.

        To create buy orders, you must have sufficient balance including fees.
        Available balance > price * quantity * (1 + takeLiquidityRate)

        Order result status

        For orders with timeInForce = IOC or FOK,
        the REST API returns final order state: filled or expired.

        If order can be instantly executed,
        then the REST API returns a status of filled or partiallyFilled in the order's info.

        Args:
            symbol (Symbol): Trading symbol.
            side (OrderSide): Trade side. Accepted values: sell or buy.
            quantity (str): order quantity.
            price (str): Order price. Required for limit order types.
            type_ (Optional[OrderType], optional):
                Accepted values: limit, market, stopLimit, stopMarket. Default value: limit.
            time_in_force (Optional[TimeInForce], optional):
                Accepted values: GTC, IOC, FOK, Day, GTD. Default value: GTC.
            stop_price (Optional[str], optional): Required for stop-limit and stop-market orders.
            expire_time (Optional[Datetime], optional): Required for orders
                with `time_in_force` = "GTD".
            strict_validate (Optional[bool], optional): Price and quantity
                will be checked for incrementation within the symbol’s tick size
                and quantity step. See the symbol's tickSize and quantityIncrement.
            post_only (Optional[bool], optional): If your pkost-only order
                causes a match with a pre-existing order as a taker,
                then the order will be cancelled.
            client_order_id (Optional[str], optional): If it is skipped,
                it will be generated by the Server.
                Uniqueness must be guaranteed within a single trading day,
                including all active orders.

        Returns:
            RequesterResponse
        """

        req = self._creator.create_new_order_request(
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price,
            type_=type_,
            time_in_force=time_in_force,
            stop_price=stop_price,
            expire_time=expire_time,
            strict_validate=strict_validate,
            post_only=post_only,
            client_order_id=client_order_id
        )
        res = await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)
        return res

    async def cancel_orders(self, symbol: Optional[Symbol] = None) -> RequesterResponse:
        """Cancel all active orders, or all active orders for a specified symbol.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            symbol (Optional[Symbol], optional): Optional parameter
                to filter active orders by symbol.

        Returns:
            RequesterResponse
        """

        req = self._creator.create_cancel_orders_request(
            symbol=symbol)
        res = await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)
        return res

    async def cancel_order(self, client_order_id: str) -> RequesterResponse:
        """Cancel active order by `client_order_id`.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            client_order_id (str)

        Returns:
            RequesterResponse
        """

        req = self._creator.create_cancel_order_request(
            client_order_id=client_order_id)
        res = await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)
        return res

    async def get_fee(self, symbol: Symbol) -> RequesterResponse:
        """Gets personal trading commission rate for certain symbol.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            symbol (Symbol)

        Returns:
            RequesterResponse
        """

        req = self._creator.create_get_fee_request(
            symbol=symbol)
        res = await self.request(
            method=req.method, url=req.url,
            headers=req.headers, data=req.data, json=req.json)
        return res
