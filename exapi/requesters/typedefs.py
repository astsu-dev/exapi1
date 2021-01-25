"""Has type definitions for exchange requesters."""

from typing import Dict

import aiohttp

RequesterResponse = aiohttp.ClientResponse
Session = aiohttp.ClientSession
Headers = Dict[str, str]
Params = Dict[str, str]
