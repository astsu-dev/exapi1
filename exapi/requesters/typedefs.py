"""Has type definitions for exchange requesters."""

from typing import Dict

import aiohttp

RequesterResponse = aiohttp.ClientResponse
Headers = Dict[str, str]
Params = Dict[str, str]
