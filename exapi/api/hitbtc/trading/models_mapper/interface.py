"""Has hitbtc trading models mapper interface."""

from exapi.models.hitbtc import (HitbtcOrderModel, HitbtcOrders,
                                 HitbtcRawOrderModel, HitbtcRawOrders,
                                 HitbtcRawTradingCurrencyBalances,
                                 HitbtcRawTradingFeeModel,
                                 HitbtcTradingCurrencyBalances,
                                 HitbtcTradingFeeModel)
from exapi.models.hitbtc.mapper.base import IHitbtcBaseModelsMapper


class IHitbtcTradingModelsMapper(IHitbtcBaseModelsMapper):
    """Has methods for mapping hitbtc trading json models
    to hitbtc dataclass models.
    """

    def map_to_order(self, raw_order: HitbtcRawOrderModel) -> HitbtcOrderModel:
        """Maps order json to order model.

        Args:
            raw_order (HitbtcRawOrderModel)

        Returns:
            HitbtcOrderModel
        """

    def map_to_orders(self, raw_orders: HitbtcRawOrders) -> HitbtcOrders:
        """Maps orders json to list of order.

        Args:
            raw_orders (HitbtcRawOrders)

        Returns:
            HitbtcOrders
        """

    def map_to_trading_balance(self, raw_balance: HitbtcRawTradingCurrencyBalances
                               ) -> HitbtcTradingCurrencyBalances:
        """Maps trading balance json to trading balance.

        Args:
            raw_balance (HitbtcRawTradingCurrencyBalances)

        Returns:
            HitbtcTradingCurrencyBalances
        """

    def map_to_trading_fee(self, raw_fee: HitbtcRawTradingFeeModel) -> HitbtcTradingFeeModel:
        """Maps orders json to list of order.

        Args:
            raw_orders (HitbtcRawOrders)

        Returns:
            HitbtcOrders
        """
