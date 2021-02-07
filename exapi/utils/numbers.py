"""Has utils for work with numbers."""

import decimal
from decimal import Decimal
from typing import Optional


def decimal_to_str(n: Decimal, precision: Optional[int] = None) -> str:
    """Converts decimal `n` number to string with `precision`.

    Args:
        n (Decimal)
        precision (Optional[int]): number of digits after comma.
            If None will be used number own precision.

    Returns:
        str
    """

    with decimal.localcontext() as ctx:
        ctx.rounding = decimal.ROUND_DOWN
        res = f"{n:.{precision}f}" if precision is not None else f"{n:f}"
    return res
