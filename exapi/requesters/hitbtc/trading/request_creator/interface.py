"""Has hitbtc trading request creator interface."""

from typing import Optional, Protocol

from exapi.requesters.request import Request
from exapi.typedefs.hitbtc import (Datetime, OrderSide, OrderType, Symbol,
                                   TimeInForce)


class IHitbtcTradingRequestCreator(Protocol):
    """Has methods for creating requests to hitbtc trading api."""

    def create_get_trading_balance_request(self) -> Request:
        """Creates a request for get trading balance.

        Requires the "Orderbook, History, Trading balance" API key Access Right.

        Returns:
            Request
        """

    def create_get_active_orders_request(self, symbol: Optional[Symbol]) -> Request:
        """Creates a request for get active orders.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            symbol (Symbol)

        Returns:
            Request
        """

    def create_get_active_order_request(self, client_order_id: str,
                                        wait: Optional[int] = None
                                        ) -> Request:
        """Creates a request for get active order endpoint.

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
            Request
        """

    def create_new_order_request(self, symbol: Symbol,
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
                                 ) -> Request:
        """Creates a request for create new order endpoint.

        Requires the "Place/cancel orders" API key Access Right.

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
            client_order_id (Optional[str], optional): If it is skipped,
                it will be generated by the Server.
                Uniqueness must be guaranteed within a single trading day,
                including all active orders.

        Returns:
            Request
        """

    def create_cancel_orders_request(self, symbol: Optional[Symbol] = None) -> Request:
        """Creates a request for cancel orders endpoint.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            symbol (Optional[Symbol], optional): Optional parameter
                to filter active orders by symbol.

        Returns:
            Request
        """

    def create_cancel_order_request(self, client_order_id: str) -> Request:
        """Creates a request for cancel order endpoint.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            client_order_id (ClientOrderID)

        Returns:
            Request
        """

    def create_get_fee_request(self, symbol: Symbol) -> Request:
        """Creates a request for get trading commission endpoint.

        Requires the "Place/cancel orders" API key Access Right.

        Args:
            symbol (Symbol)

        Returns:
            Request
        """
