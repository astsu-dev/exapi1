import base64
import hashlib
import hmac
from unittest.mock import patch

import pytest
from exapi.requesters.hitbtc.auth import HitbtcAuth


@pytest.fixture(scope="module")
def auth() -> HitbtcAuth:
    return HitbtcAuth("aa", "aa")


def test__create_signature_payload(auth: HitbtcAuth) -> None:
    method = "GET"
    timestamp = "151515"
    url_path = "/api/2/public/currency"
    url_query = "test=test"
    body = None

    assert auth._create_signature_payload(
        method, timestamp, url_path, url_query, body) == method + timestamp + url_path + "?" + url_query

    method = "GET"
    timestamp = "151515"
    url_path = "/api/2/public/currency"
    url_query = ""
    body = None

    assert auth._create_signature_payload(
        method, timestamp, url_path, url_query, body) == method + timestamp + url_path

    method = "GET"
    timestamp = "151515"
    url_path = "/api/2/public/currency"
    url_query = ""
    body = "test=test"

    assert auth._create_signature_payload(
        method, timestamp, url_path, url_query, body) == method + timestamp + url_path + body


def test__create_signature(auth: HitbtcAuth) -> None:
    method = "GET"
    timestamp = "151515"
    url_path = "/api/2/public/currency"
    url_query = "test=test"
    msg = method + timestamp + url_path + "?" + url_query
    signature = hmac.new("aa".encode("utf-8"),
                         msg.encode("utf-8"), hashlib.sha256).hexdigest()
    assert auth._create_signature(msg) == signature


def test__create_auth_string(auth: HitbtcAuth) -> None:
    en = "utf-8"

    method = "GET"
    timestamp = "151515"
    url_path = "/api/2/public/currency"
    url_query = "test=test"
    msg = method + timestamp + url_path + "?" + url_query
    signature = hmac.new("aa".encode("utf-8"),
                         msg.encode("utf-8"), hashlib.sha256).hexdigest()
    auth_payload = ":".encode(en).join(
        ["aa".encode(en), timestamp.encode(en), signature.encode(en)])

    auth_string = "HS256 " + base64.b64encode(auth_payload).decode(en)

    assert auth_string == auth._create_auth_string(timestamp, signature)


def test_sign(auth: HitbtcAuth) -> None:
    en = "utf-8"

    method = "GET"
    timestamp = "151515"
    url_path = "/api/2/public/currency"
    url_query = "test=test"
    msg = method + timestamp + url_path + "?" + url_query
    signature = hmac.new("aa".encode("utf-8"),
                         msg.encode("utf-8"), hashlib.sha256).hexdigest()
    auth_payload = ":".encode(en).join(
        ["aa".encode(en), timestamp.encode(en), signature.encode(en)])

    auth_string = "HS256 " + base64.b64encode(auth_payload).decode(en)

    with patch("exapi.requesters.hitbtc.auth.HitbtcAuth.get_timestamp") as get_timestamp:
        get_timestamp.return_value = timestamp
        assert auth.sign(method, url_path, url_query) == {
            "Authorization": auth_string}
