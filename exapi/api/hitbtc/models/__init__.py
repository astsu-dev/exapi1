"""Has hitbtc models."""

from .candle import HitbtcCandleModel, HitbtcCandles, HitbtcSymbolCandles
from .currency import HitbtcCurrencies, HitbtcCurrencyModel
from .error import HitbtcErrorModel
from .order_book import (HitbtcOrderBookModel, HitbtcOrderBookOrderModel,
                         HitbtcOrderBooks)
from .symbol import HitbtcSymbolModel, HitbtcSymbols
from .ticker import HitbtcTickerModel, HitbtcTickers
from .trade import HitbtcSymbolTrades, HitbtcTradeModel, HitbtcTrades
