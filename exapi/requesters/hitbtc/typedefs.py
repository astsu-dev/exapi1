"""Has type definitions for hitbtc requesters."""

from typing import Iterable, Literal, Union

Symbol = str
Currency = str
Symbols = Iterable[Symbol]
Currencies = Iterable[Currency]
SortDirection = Literal["ASC", "DESC"]
SortBy = Literal["id", "timestamp"]
Datetime = str
IntervalValue = Union[Datetime, int]
CandlesPeriod = Literal["M1", "M3", "M5",
                        "M15", "M30", "H1", "H4", "D1", "D7", "1M"]
