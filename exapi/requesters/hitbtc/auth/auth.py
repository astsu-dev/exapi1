"""Has hitbtc authorizator."""

import base64
import hashlib
import hmac
import time
from typing import Final, Optional

from exapi.requesters.hitbtc.auth.interface import IHitbtcAuth
from exapi.requesters.hitbtc.auth.typedefs import HitbtcAuthHeaders


class HitbtcAuth(IHitbtcAuth):
    """Has methods for authorization a request to hitbtc."""

    _ENCODING: Final[str] = "utf-8"

    def __init__(self, API_KEY: str, API_SECRET: str) -> None:
        self._API_KEY: Final[str] = API_KEY
        self._API_SECRET: Final[str] = API_SECRET

    def sign(self, method: str,
             url_path: str,
             url_query: str,
             body: Optional[str] = None
             ) -> HitbtcAuthHeaders:
        """Returns headers with the Authorization header.

        Args:
            method (str): http method.
            url_path (str): url path.
            url_query (str): url query.
            body (str): http body.

        Returns:
            HitbtcAuthHeaders
        """

        ts = self.get_timestamp()

        sign_payload = self._create_signature_payload(
            method=method, timestamp=ts, url_path=url_path, url_query=url_query, body=body)
        sign = self._create_signature(payload=sign_payload)

        auth_string = self._create_auth_string(timestamp=ts, signature=sign)

        headers: HitbtcAuthHeaders = {
            "Authorization": auth_string
        }

        return headers

    @staticmethod
    def get_timestamp() -> str:
        """Returns current timestamp in seconds.

        Returns:
            str
        """

        return str(int(time.time()))

    def _create_signature(self, payload: str) -> str:
        """Creates signature from payload.

        Args:
            payload (str): (method + timestamp + url_path + url_query + body).

        Returns:
            str
        """

        en = self._ENCODING
        signature = hmac.new(
            self._API_SECRET.encode(en),
            payload.encode(en), hashlib.sha256).hexdigest()
        return signature

    def _create_signature_payload(self, method: str,
                                  timestamp: str,
                                  url_path: str,
                                  url_query: str,
                                  body: Optional[str] = None
                                  ) -> str:
        """Creates payload for signature creating.

        Payload is a result of concatenating method, timestamp, url_path, url_query, body.

        Args:
            method (str): http method
            timestamp (str): timestamp in seconds.
            url_path (str): url path
            url_query (str): url query
            body (Optional[str], optional): http body

        Returns:
            str
        """

        payload = method + timestamp + url_path
        if url_query:
            payload += "?" + url_query
        if body is not None:
            payload += body

        return payload

    def _create_auth_string(self, timestamp: str, signature: str) -> str:
        """Creates auth string.

        Auth string is a result of concatenation
        api key, timestamp, signature encoded by base64 encoding.

        Args:
            timestamp (str): timestamp in seconds.
            signature (str): signature.

        Returns:
            str
        """

        en = self._ENCODING

        auth_payload = ":".encode(en).join(
            [self._API_KEY.encode(en), timestamp.encode(en), signature.encode(en)])
        auth_string = "HS256 " + base64.b64encode(auth_payload).decode(en)

        return auth_string
