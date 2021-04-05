"""Has hitbtc currency model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional, TypedDict

from exapi.typedefs.hitbtc import Currency


class HitbtcRawCurrencyModel(TypedDict):
    """Currency json model.

    Args:
        id (Currency)
        fullName (str)
        crypto (bool)
        payinEnabled (bool)
        payinPaymentId (bool)
        payinConfirmations (int)
        payoutEnabled (bool)
        payoutIsPaymentId (bool)
        transferEnabled (bool)
        delisted (bool)
        payoutFee (str, optional)
        precisionPayout (int)
        precisionTransfer (int)
    """

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
        precision_payout (int)
        precision_transfer (int)
        payout_fee (Optional[Decimal]). Defaults to None.
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
    precision_payout: int
    precision_transfer: int
    payout_fee: Optional[Decimal] = None


HitbtcRawCurrencies = List[HitbtcRawCurrencyModel]
HitbtcCurrencies = List[HitbtcCurrencyModel]
