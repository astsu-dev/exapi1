from exapi.utils.url import create_query_string


def test_create_query_string() -> None:
    assert create_query_string(
        {"price": "1.1", "qty": "2.3"}) == "price=1.1&qty=2.3"
