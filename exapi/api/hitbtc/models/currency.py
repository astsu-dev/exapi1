"""Has hitbtc currency model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List

from exapi.requesters.hitbtc.typedefs import Currency


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
        payout_is_paymentId (bool)
        transfer_enabled (bool)
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
    payout_is_paymentId: bool
    transfer_enabled: bool
    delisted: bool
    payout_fee: Decimal
    payout_minimal_amount: Decimal
    precision_payout: int
    precision_transfer: int


HitbtcCurrencies = List[HitbtcCurrencyModel]
