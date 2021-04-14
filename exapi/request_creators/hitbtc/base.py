"""Has hitbtc base request creator."""

from exapi.request_creators.base import BaseRequestCreator


class HitbtcBaseRequestCreator(BaseRequestCreator):
    """Hitbtc base request creator.

    Has ROOT_URL field which contains root hitbtc api url.
    """

    BASE_URL: str = "https://api.hitbtc.com"
