"""Has hitbtc models."""

from exapi.models.hitbtc.candle import (HitbtcCandleModel, HitbtcCandles, HitbtcRawCandleModel,
                                        HitbtcRawCandles, HitbtcRawSymbolCandles,
                                        HitbtcSymbolCandles)
from exapi.models.hitbtc.currency import (HitbtcCurrencies, HitbtcCurrencyModel,
                                          HitbtcRawCurrencies, HitbtcRawCurrencyModel)
from exapi.models.hitbtc.error import (HitbtcErrorModel, HitbtcRawDetailedErrorModel,
                                       HitbtcRawErrorModel)
from exapi.models.hitbtc.order import (HitbtcOrderModel, HitbtcOrders, HitbtcRawOrderModel,
                                       HitbtcRawOrders)
from exapi.models.hitbtc.order_book import (HitbtcOrderBookModel, HitbtcOrderBookOrderModel,
                                            HitbtcOrderBooks, HitbtcRawOrderBookModel,
                                            HitbtcRawOrderBookOrderModel, HitbtcRawOrderBooks)
from exapi.models.hitbtc.symbol import (HitbtcRawSymbolModel, HitbtcRawSymbols, HitbtcSymbolModel,
                                        HitbtcSymbols)
from exapi.models.hitbtc.ticker import (HitbtcRawTickerModel, HitbtcRawTickers, HitbtcTickerModel,
                                        HitbtcTickers)
from exapi.models.hitbtc.trade import (HitbtcRawSymbolTrades, HitbtcRawTradeModel,
                                       HitbtcRawTrades, HitbtcSymbolTrades, HitbtcTradeModel,
                                       HitbtcTrades)
from exapi.models.hitbtc.trading_balance import (HitbtcRawTradingCurrencyBalanceModel,
                                                 HitbtcRawTradingCurrencyBalances,
                                                 HitbtcTradingCurrencyBalanceModel,
                                                 HitbtcTradingCurrencyBalances)
from exapi.models.hitbtc.trading_fee import HitbtcRawTradingFeeModel, HitbtcTradingFeeModel
