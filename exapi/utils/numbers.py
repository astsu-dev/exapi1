"""Has utils for work with numbers."""

import decimal
from decimal import Decimal


def decimal_to_str(n: Decimal, precision: int) -> str:
    """Converts decimal `n` number to string with `precision`.

    Args:
        n (Decimal)
        precision (int): number of digits after comma.

    Returns:
        str
    """

    with decimal.localcontext() as ctx:
        ctx.rounding = decimal.ROUND_DOWN
        res = f"{n:.{precision}f}"
    return res
