from dataclasses import dataclass
from typing import TypedDict

from exapi.typedefs.binance import AccountType

from .balance import BinanceCurrencyBalances, BinanceCurrencyBalancesJson


class BinanceAccountInfoJson(TypedDict):
    makerCommission: int
    takerCommission: int
    buyerCommission: int
    sellerCommission: int
    canTrade: bool
    canWithdraw: bool
    canDeposit: bool
    updateTime: int
    accountType: AccountType
    balances: BinanceCurrencyBalancesJson


@dataclass(frozen=True)
class BinanceAccountInfoModel:
    """Binance account information model.

    Args:
        maker_commission (int)
        taker_commission (int)
        buyer_commission (int)
        seller_commission (int)
        can_trade (bool)
        can_withdraw (bool)
        can_deposit (bool)
        update_time (int)
        account_type (AccountType)
        balances (BinanceBalancesJson)
    """

    maker_commission: int
    taker_commission: int
    buyer_commission: int
    seller_commission: int
    can_trade: bool
    can_withdraw: bool
    can_deposit: bool
    update_time: int
    account_type: AccountType
    balances: BinanceCurrencyBalances
