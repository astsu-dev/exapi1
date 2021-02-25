"""Has binance rate limits models."""

from dataclasses import dataclass
from typing import List, Literal, TypedDict, Union

from exapi.models.binance.typedefs import RateLimitInterval


class BinanceRequestWeightRateLimitJson(TypedDict):
    rateLimitType: Literal["REQUEST_WEIGHT"]
    interval: RateLimitInterval
    intervalNum: int
    limit: int


@dataclass(frozen=True)
class BinanceRequestWeightRateLimitModel:
    """Request weight rate limit.

    Args:
        rate_limit_type (Literal["REQUEST_WEIGHT"])
        interval (RateLimitInterval): second, minute, day.
        interval_num (int): number of `interval`.
        limit (int): weight per `interval_num` `intervals`.
    """

    rate_limit_type: Literal["REQUEST_WEIGHT"]
    interval: RateLimitInterval
    interval_num: int
    limit: int


class BinanceOrdersRateLimitJson(TypedDict):
    rateLimitType: Literal["ORDERS"]
    interval: RateLimitInterval
    intervalNum: int
    limit: int


@dataclass(frozen=True)
class BinanceOrdersRateLimitModel:
    """Orders rate limit.

    Args:
        rate_limit_type (Literal["ORDERS"])
        interval (RateLimitInterval): second, minute, day.
        interval_num (int): number of `interval`.
        limit (int): number of orders per `interval_num` `intervals`.
    """

    rate_limit_type: Literal["ORDERS"]
    interval: RateLimitInterval
    interval_num: int
    limit: int


class BinanceRawRequestsRateLimitJson(TypedDict):
    rateLimitType: Literal["RAW_REQUESTS"]
    interval: RateLimitInterval
    intervalNum: int
    limit: int


@dataclass(frozen=True)
class BinanceRawRequestsRateLimitModel:
    """Raw requests rate limit.

    Args:
        rate_limit_type (Literal["RAW_REQUESTS"])
        interval (RateLimitInterval): second, minute, day.
        interval_num (int): number of `interval`.
        limit (int): number of raw requests per `interval_num` `intervals`.
    """

    rate_limit_type: Literal["RAW_REQUESTS"]
    interval: RateLimitInterval
    interval_num: int
    limit: int


BinanceRateLimitJson = Union[
    BinanceRequestWeightRateLimitJson,
    BinanceOrdersRateLimitJson,
    BinanceRawRequestsRateLimitJson]
BinanceRateLimitsJson = List[BinanceRateLimitJson]
BinanceRateLimitModel = Union[
    BinanceRequestWeightRateLimitModel,
    BinanceOrdersRateLimitModel,
    BinanceRawRequestsRateLimitModel]
BinanceRateLimits = List[BinanceRateLimitModel]
