"""Has hitbtc models."""

from .candle import (HitbtcCandleModel, HitbtcCandles, HitbtcRawCandleModel,
                     HitbtcRawCandles, HitbtcRawSymbolCandles,
                     HitbtcSymbolCandles)
from .currency import (HitbtcCurrencies, HitbtcCurrencyModel,
                       HitbtcRawCurrencies, HitbtcRawCurrencyModel)
from .error import (HitbtcErrorModel, HitbtcRawDetailedErrorModel,
                    HitbtcRawErrorModel)
from .order import (HitbtcOrderModel, HitbtcOrders, HitbtcRawOrderModel,
                    HitbtcRawOrders)
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
from .trading_balance import (HitbtcRawTradingCurrencyBalanceModel,
                              HitbtcRawTradingCurrencyBalances,
                              HitbtcTradingCurrencyBalanceModel,
                              HitbtcTradingCurrencyBalances)
from .trading_fee import HitbtcRawTradingFeeModel, HitbtcTradingFeeModel
