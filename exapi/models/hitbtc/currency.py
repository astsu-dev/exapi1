"""Has hitbtc currency model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict

from .typedefs import Currency


class HitbtcRawCurrencyModel(TypedDict):
    """Currency json model."""

    id: Currency
    fullName: str
    crypto: bool
    payinEnabled: bool
    payinPaymentId: bool
    payinConfirmations: int
    payoutEnabled: bool
    payoutIsPaymentId: bool
    transferEnabled: bool
    delisted: bool
    payoutFee: str
    payoutMinimalAmount: str
    precisionPayout: int
    precisionTransfer: int


@dataclass(frozen=True)
class HitbtcCurrencyModel:
    """Hitbtc currency model.

    Args:
        id (Currency): currency id
        full_name (str)
        crypto (bool)
        payin_enabled (bool)
        payin_payment_id (bool)
        payin_confirmations (int)
        payout_enabled (bool)
        payout_is_payment_id (bool)
        transfer_enabled (bool)k
        delisted (bool)
        payout_fee (Decimal)
        payout_minimal_amount (Decimal)
        precision_payout (int)
        precision_transfer (int)
    """

    id: Currency
    full_name: str
    crypto: bool
    payin_enabled: bool
    payin_payment_id: bool
    payin_confirmations: int
    payout_enabled: bool
    payout_is_payment_id: bool
    transfer_enabled: bool
    delisted: bool
    payout_fee: Decimal
    payout_minimal_amount: Decimal
    precision_payout: int
    precision_transfer: int


HitbtcRawCurrencies = List[HitbtcRawCurrencyModel]
HitbtcCurrencies = List[HitbtcCurrencyModel]
