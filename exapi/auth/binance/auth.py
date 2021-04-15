"""Has binance auth."""

import hashlib
import hmac

from exapi.auth.binance.interface import IBinanceAuth
from exapi.auth.binance.key import IBinanceKeyAuth
from exapi.auth.binance.result import BinanceAuthResult
from exapi.requesters.typedefs import Params
from exapi.utils.url import create_query_string


class BinanceAuth(IBinanceAuth):
    """Has methods for auth requests to binance api."""

    def __init__(self, key_auth: IBinanceKeyAuth, api_secret: str) -> None:
        self._key_auth = key_auth
        self._api_secret = api_secret

    def create_signature(self, params: Params, body: str = "") -> str:
        """Creates signature from query string and request body.

        Args:
            params (Params)
            body (str, optional)

        Returns:
            str
        """

        en = "utf-8"

        query_string = create_query_string(params)
        total_params = query_string + body

        key = self._api_secret.encode(en)
        msg = total_params.encode(en)
        signature = hmac.new(key, msg, hashlib.sha256).hexdigest()

        return signature

    def sign(self, params: Params, body: str = "") -> BinanceAuthResult:
        """Returns headers with api key and query string with signature.

        Args:
            params (Params): request params.
            body (str)

        Returns:
            BinanceAuthResult
        """

        headers = self._key_auth.sign()
        signature = self.create_signature(params, body)
        params = {**params, "signature": signature}

        return BinanceAuthResult(headers=headers, params=params)
