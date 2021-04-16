"""Has type definitions for binance market data api."""

from typing import Union

from exapi.models.binance import (BinanceOrderBookTickerModel,
                                  BinanceOrderBookTickers,
                                  BinancePriceTickerModel, BinancePriceTickers,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTickersPriceChangeStat)

BinanceOrderBookTickerModelOrTickers = Union[BinanceOrderBookTickerModel,
                                             BinanceOrderBookTickers]
BinanceTickerPriceChangeStatModelOrTickers = Union[
    BinanceTickerPriceChangeStatModel, BinanceTickersPriceChangeStat]
BinancePriceTickerModelOrTickers = Union[BinancePriceTickerModel,
                                         BinancePriceTickers]
