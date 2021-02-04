"""Has hitbtc models."""

from .candle import (HitbtcCandleModel, HitbtcCandles, HitbtcRawCandleModel,
                     HitbtcRawCandles, HitbtcRawSymbolCandles,
                     HitbtcSymbolCandles)
from .currency import (HitbtcCurrencies, HitbtcCurrencyModel,
                       HitbtcRawCurrencies, HitbtcRawCurrencyModel)
from .error import (HitbtcErrorModel, HitbtcRawDetailedErrorModel,
                    HitbtcRawErrorModel)
from .order import HitbtcOrderModel, HitbtcRawOrderModel
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
from .trading_balance import (HitbtcCurrencyTradingBalanceModel,
                              HitbtcCurrencyTradingBalances,
                              HitbtcRawCurrencyTradingBalanceModel,
                              HitbtcRawCurrencyTradingBalances)
from .trading_fee import HitbtcRawTradingFeeModel, HitbtcTradingFeeModel