"""Has hitbtc models."""

from .candle import (HitbtcCandleModel, HitbtcCandles, HitbtcRawCandleModel,
                     HitbtcRawCandles, HitbtcRawSymbolCandles,
                     HitbtcSymbolCandles)
from .currency import (HitbtcCurrencies, HitbtcCurrencyModel,
                       HitbtcRawCurrencies, HitbtcRawCurrencyModel)
from .error import (HitbtcErrorModel, HitbtcRawDetailedErrorModel,
                    HitbtcRawErrorModel)
from .order_book import (HitbtcOrderBookModel, HitbtcOrderBookOrderModel,
                         HitbtcOrderBooks, HitbtcRawOrderBookModel,
                         HitbtcRawOrderBookOrderModel, HitbtcRawOrderBooks)
from .symbol import (HitbtcRawSymbolModel, HitbtcRawSymbols, HitbtcSymbolModel,
                     HitbtcSymbols)
from .ticker import (HitbtcRawTickerModel, HitbtcRawTickers, HitbtcTickerModel,
                     HitbtcTickers)
from .trade import (HitbtcRawSymbolTrades, HitbtcRawTradeModel,
                    HitbtcRawTrades, HitbtcSymbolTrades, HitbtcTradeModel,
                    HitbtcTrades)
