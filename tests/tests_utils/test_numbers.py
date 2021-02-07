from decimal import Decimal

from exapi.utils import decimal_to_str


def test_decimal_to_str() -> None:
    assert decimal_to_str(Decimal("0.111"), 8) == "0.11100000"
    assert decimal_to_str(Decimal("0.111"), 0) == "0"
    assert decimal_to_str(Decimal("0.111"), 8) == "0.11100000"
    assert decimal_to_str(Decimal("1.15e-12"), 14) == "0.00000000000115"
    assert decimal_to_str(Decimal("1.15e-12"), 12) == "0.000000000001"
    assert decimal_to_str(Decimal("0.119"), 2) == "0.11"
    assert decimal_to_str(Decimal("-0.119"), 2) == "-0.11"  # test on not floor

    assert decimal_to_str(Decimal("0.0001000")) == "0.0001000"
    assert decimal_to_str(Decimal("1e-10")) == "0.0000000001"
    assert decimal_to_str(Decimal("1.15e-12")) == "0.00000000000115"
