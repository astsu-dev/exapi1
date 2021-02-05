"""Has hitbtc trading requester interface."""

from decimal import Decimal
from typing import Optional, Protocol

from exapi.models.hitbtc import (HitbtcCurrencyTradingBalances,
                                 HitbtcOrderModel, HitbtcOrders,
                                 HitbtcTradingFeeModel)
from exapi.models.hitbtc.typedefs import (Datetime, OrderSide, OrderType,
                                          Symbol, TimeInForce)


class IHitbtcTradingAPI(Protocol):
    """Has methods for making requests to hitbtc trading api."""

    async def get_trading_balance(self) -> HitbtcCurrencyTradingBalances:
        """Returns the user's trading balance.

        Requires the "Orderbook, History, Trading balance" API key Access Right.

        Returns:
            HitbtcCurrencyTradingBalances
        """

    async def get_active_orders(self, symbol: Optional[Symbol] = None) -> HitbtcOrders:
        """Return a array of active orders.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            symbol (Optional[Symbol])

        Returns:
            HitbtcOrders
        """

    async def get_active_order(self, client_order_id: int,
                               wait: Optional[int] = None
                               ) -> HitbtcOrderModel:
        """Returns the order by `client_order_id`.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            client_order_id (ClientOrderID)
            wait (Optional[int], optional): Time in milliseconds.
                Max value: 60000. Default value: none.
                While using long polling request: if order is filled,
                cancelled or expired order info will be returned instantly.
                For other order statuses, actual order info
                will be returned after specified wait time.

        Returns:
            HitbtcOrderModel
        """

    async def new_order(self, symbol: Symbol,
                        side: OrderSide,
                        quantity: Decimal,
                        price: Decimal,
                        type_: Optional[OrderType] = None,
                        time_in_force: Optional[TimeInForce] = None,
                        stop_price: Optional[Decimal] = None,
                        expire_time: Optional[Datetime] = None,
                        strict_validate: Optional[bool] = None,
                        post_only: Optional[bool] = None,
                        client_order_id: Optional[int] = None,
                        ) -> HitbtcOrderModel:
        """Requires the "Place/cancel orders" API key Access Right.

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
            post_only (Optional[bool], optional): If your post-only order
                causes a match with a pre-existing order as a taker,
                then the order will be cancelled.
            client_order_id (Optional[int], optional): If it is skipped,
                it will be generated by the Server.
                Uniqueness must be guaranteed within a single trading day,
                including all active orders.

        Returns:
            HitbtcOrderModel
        """

    async def cancel_orders(self, symbol: Optional[Symbol] = None) -> HitbtcOrders:
        """Cancel all active orders, or all active orders for a specified symbol.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            symbol (Optional[Symbol], optional): Optional parameter
                to filter active orders by symbol.

        Returns:
            HitbtcOrders
        """

    async def cancel_order(self, client_order_id: int) -> HitbtcOrderModel:
        """Cancel active order by `client_order_id`.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            client_order_id (ClientOrderID)

        Returns:
            HitbtcOrderModel
        """

    async def get_fee(self, symbol: Symbol) -> HitbtcTradingFeeModel:
        """Gets personal trading commission rate for certain symbol.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            symbol (Symbol)

        Returns:
            HitbtcTradingFeeModel
        """
