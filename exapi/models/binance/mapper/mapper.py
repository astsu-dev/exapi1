"""Has binance models mapper interface."""

from decimal import Decimal

from exapi.enums.binance import (BinanceExchangeFilterType,
                                 BinanceRateLimitType, BinanceSymbolFilterType)
from exapi.models.binance import (BinanceAccountInfoJson,
                                  BinanceAccountInfoModel,
                                  BinanceAveragePriceJson,
                                  BinanceAveragePriceModel, BinanceCandleJson,
                                  BinanceCandleModel, BinanceCandles,
                                  BinanceCandlesJson,
                                  BinanceCurrencyBalanceJson,
                                  BinanceCurrencyBalanceModel,
                                  BinanceCurrencyBalances,
                                  BinanceCurrencyBalancesJson,
                                  BinanceExchangeFilterJson,
                                  BinanceExchangeFilterModel,
                                  BinanceExchangeFilters,
                                  BinanceExchangeFiltersJson,
                                  BinanceExchangeInfoJson,
                                  BinanceExchangeInfoModel,
                                  BinanceFilledOrderJson,
                                  BinanceFilledOrderModel, BinanceFilledOrders,
                                  BinanceFilledOrdersJson,
                                  BinanceIcebergPartsSymbolFilterJson,
                                  BinanceIcebergPartsSymbolFilterModel,
                                  BinanceLotSizeSymbolFilterJson,
                                  BinanceLotSizeSymbolFilterModel,
                                  BinanceMarketLotSizeSymbolFilterJson,
                                  BinanceMarketLotSizeSymbolFilterModel,
                                  BinanceMaxNumAlgoOrdersExchangeFilterJson,
                                  BinanceMaxNumAlgoOrdersExchangeFilterModel,
                                  BinanceMaxNumAlgoOrdersSymbolFilterJson,
                                  BinanceMaxNumAlgoOrdersSymbolFilterModel,
                                  BinanceMaxNumIcebergOrdersSymbolFilterJson,
                                  BinanceMaxNumIcebergOrdersSymbolFilterModel,
                                  BinanceMaxNumOrdersExchangeFilterJson,
                                  BinanceMaxNumOrdersExchangeFilterModel,
                                  BinanceMaxNumOrdersSymbolFilterJson,
                                  BinanceMaxNumOrdersSymbolFilterModel,
                                  BinanceMaxPositionSymbolFilterJson,
                                  BinanceMaxPositionSymbolFilterModel,
                                  BinanceMinNotionalSymbolFilterJson,
                                  BinanceMinNotionalSymbolFilterModel,
                                  BinanceOrderBookJson, BinanceOrderBookModel,
                                  BinanceOrderBookOrderJson,
                                  BinanceOrderBookOrderModel,
                                  BinanceOrderBookOrders,
                                  BinanceOrderBookOrdersJson,
                                  BinanceOrderBookTickerJson,
                                  BinanceOrderBookTickerModel,
                                  BinanceOrderBookTickers,
                                  BinanceOrderBookTickersJson,
                                  BinanceOrderJson, BinanceOrderModel,
                                  BinanceOrders, BinanceOrdersJson,
                                  BinancePercentPriceSymbolFilterJson,
                                  BinancePercentPriceSymbolFilterModel,
                                  BinancePingJson, BinancePingModel,
                                  BinancePriceSymbolFilterJson,
                                  BinancePriceSymbolFilterModel,
                                  BinancePriceTickerJson,
                                  BinancePriceTickerModel, BinancePriceTickers,
                                  BinancePriceTickersJson,
                                  BinanceRateLimitJson, BinanceRateLimitModel,
                                  BinanceRateLimits, BinanceRateLimitsJson,
                                  BinanceServerTimeJson,
                                  BinanceServerTimeModel,
                                  BinanceSymbolFilterJson,
                                  BinanceSymbolFilterModel,
                                  BinanceSymbolFilters,
                                  BinanceSymbolFiltersJson, BinanceSymbolJson,
                                  BinanceSymbolModel, BinanceSymbols,
                                  BinanceSymbolsJson,
                                  BinanceTickerPriceChangeStatJson,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTickersPriceChangeStat,
                                  BinanceTickersPriceChangeStatJson,
                                  BinanceTradeJson, BinanceTradeModel,
                                  BinanceTrades, BinanceTradesJson)
from exapi.models.binance.exchange_info.rate_limits import (
    BinanceOrdersRateLimitJson, BinanceOrdersRateLimitModel,
    BinanceRawRequestsRateLimitJson, BinanceRawRequestsRateLimitModel,
    BinanceRequestWeightRateLimitJson, BinanceRequestWeightRateLimitModel)

from .base import BinanceBaseModelsMapper
from .interface import IBinanceModelsMapper


class BinanceModelsMapper(IBinanceModelsMapper, BinanceBaseModelsMapper):
    """Binance models mapper interface.

    Maps json to models.
    """

    def map_to_ping(self, json: BinancePingJson) -> BinancePingModel:
        """Maps ping json to ping model.

        Args:
            json (BinancePingJson)

        Returns:
            BinancePingModel
        """

        return BinancePingModel()

    def map_to_server_time(self, json: BinanceServerTimeJson) -> BinanceServerTimeModel:
        """Maps server time json to server time model.

        Args:
            json (BinanceServerTimeJson)

        Returns:
            BinanceServerTimeModel
        """

        return BinanceServerTimeModel(server_time=json["serverTime"])

    def map_to_average_price(self, json: BinanceAveragePriceJson) -> BinanceAveragePriceModel:
        """Maps average price json to average price model.

        Args:
            json (BinanceAveragePriceJson)

        Returns:
            BinanceAveragePriceModel
        """

        res = BinanceAveragePriceModel(
            mins=json["mins"],
            price=Decimal(json["price"]))
        return res

    def map_to_candle(self, json: BinanceCandleJson) -> BinanceCandleModel:
        """Maps candle json to candle model.

        Args:
            json (BinanceCandleJson)

        Returns:
            BinanceCandleModel
        """

        res = BinanceCandleModel(
            open_time=json[0],
            open=Decimal(json[1]),
            high=Decimal(json[2]),
            low=Decimal(json[3]),
            close=Decimal(json[4]),
            volume=Decimal(json[5]),
            close_time=json[6],
            quote_volume=Decimal(json[7]),
            trades_num=json[8],
            taker_buy_base_volume=Decimal(json[9]),
            taker_buy_quote_volume=Decimal(json[10]),
            ignore=Decimal(json[11]))
        return res

    def map_to_candles(self, json: BinanceCandlesJson) -> BinanceCandles:
        """Maps candles json to candles model.

        Args:
            json (BinanceCandlesJson)

        Returns:
            BinanceCandles
        """

        res = list(map(self.map_to_candle, json))
        return res

    def map_to_order_book_ticker(self, json: BinanceOrderBookTickerJson
                                 ) -> BinanceOrderBookTickerModel:
        """Maps order book ticker json to order book ticker model.

        Args:
            json (BinanceOrderBookTickerJson)

        Returns:
            BinanceOrderBookTickerModel
        """

        res = BinanceOrderBookTickerModel(
            symbol=json["symbol"],
            bid_price=Decimal(json["bidPrice"]),
            bid_qty=Decimal(json["bidQty"]),
            ask_price=Decimal(json["askPrice"]),
            ask_qty=Decimal(json["askQty"]))
        return res

    def map_to_order_book_tickers(self, json: BinanceOrderBookTickersJson
                                  ) -> BinanceOrderBookTickers:
        """Maps order book tickers json to order book tickers model.

        Args:
            json (BinanceOrderBookTickersJson)

        Returns:
            BinanceOrderBookTickersModel
        """

        res = list(map(self.map_to_order_book_ticker, json))
        return res

    def map_to_order_book_order(self, json: BinanceOrderBookOrderJson
                                ) -> BinanceOrderBookOrderModel:
        """Maps order book order json to order book order model.

        Args:
            json (BinanceOrderBookOrderJson)

        Returns:
            BinanceOrderBookOrderModel
        """

        res = BinanceOrderBookOrderModel(
            price=Decimal(json[0]),
            quantity=Decimal(json[1]))
        return res

    def map_to_order_book_orders(self, json: BinanceOrderBookOrdersJson
                                 ) -> BinanceOrderBookOrders:
        """Maps order book orders json to order book orders model.

        Args:
            json (BinanceOrderBookOrdersJson)

        Returns:
            BinanceOrderBookOrders
        """

        res = list(map(self.map_to_order_book_order, json))
        return res

    def map_to_order_book(self, json: BinanceOrderBookJson) -> BinanceOrderBookModel:
        """Maps order book json to order book model.

        Args:
            json (BinanceOrderBookJson)

        Returns:
            BinanceOrderBookModel
        """

        res = BinanceOrderBookModel(
            last_update_id=json["lastUpdateId"],
            bids=self.map_to_order_book_orders(json["bids"]),
            asks=self.map_to_order_book_orders(json["asks"]))
        return res

    def map_to_filled_order(self, json: BinanceFilledOrderJson) -> BinanceFilledOrderModel:
        """Maps filled order json to filled order model.

        Args:
            json (BinanceFilledOrderJson)

        Returns:
            BinanceFilledOrderModel
        """

        res = BinanceFilledOrderModel(
            price=Decimal(json["price"]),
            qty=Decimal(json["qty"]),
            commission=Decimal(json["commission"]),
            commission_asset=json["commissionAsset"])
        return res

    def map_to_filled_orders(self, json: BinanceFilledOrdersJson) -> BinanceFilledOrders:
        """Maps filled orders json to filled orders model.

        Args:
            json (BinanceFilledOrdersJson)

        Returns:
            BinanceFilledOrders
        """

        res = list(map(self.map_to_filled_order, json))
        return res

    def map_to_order(self, json: BinanceOrderJson) -> BinanceOrderModel:
        """Maps order json to order model.

        Args:
            json (BinanceOrderJson)

        Returns:
            BinanceOrderModel
        """

        raw_price = json.get("price")
        price = Decimal(raw_price) if raw_price is not None else raw_price

        raw_orig_qty = json.get("origQty")
        orig_qty = Decimal(
            raw_orig_qty) if raw_orig_qty is not None else raw_orig_qty

        raw_executed_qty = json.get("executedQty")
        executed_qty = Decimal(
            raw_executed_qty) if raw_executed_qty is not None else raw_executed_qty

        raw_cummulative_quote_qty = json.get("cummulativeQuoteQty")
        cummulative_quote_qty = (Decimal(raw_cummulative_quote_qty) if raw_cummulative_quote_qty is not None
                                 else raw_cummulative_quote_qty)

        status = json.get("status")
        time_in_force = json.get("timeInForce")
        type_ = json.get("type")
        side = json.get("side")

        raw_fills = json.get("fills")
        fills = self.map_to_filled_orders(
            raw_fills) if raw_fills is not None else raw_fills

        res = BinanceOrderModel(
            symbol=json["symbol"],
            order_id=json["orderId"],
            order_list_id=json["orderListId"],
            client_order_id=json["clientOrderId"],
            transact_time=json["transactTime"],
            price=price,
            orig_qty=orig_qty,
            executed_qty=executed_qty,
            cummulative_quote_qty=cummulative_quote_qty,
            status=status,
            time_in_force=time_in_force,
            type=type_,
            side=side,
            fills=fills)
        return res

    def map_to_orders(self, json: BinanceOrdersJson) -> BinanceOrders:
        """Maps orders json to orders model.

        Args:
            json (BinanceOrdersJson)

        Returns:
            BinanceOrders
        """

        res = list(map(self.map_to_order, json))
        return res

    def map_to_price_ticker(self, json: BinancePriceTickerJson) -> BinancePriceTickerModel:
        """Maps price ticker json to price ticker model.

        Args:
            json (BinancePriceTickerJson)

        Returns:
            BinancePriceTickerModel
        """

        res = BinancePriceTickerModel(
            symbol=json["symbol"],
            price=Decimal(json["price"]))
        return res

    def map_to_price_tickers(self, json: BinancePriceTickersJson) -> BinancePriceTickers:
        """Maps price tickers json to price tickers model.

        Args:
            json (BinancePriceTickersJson)

        Returns:
            BinancePriceTickers
        """

        res = list(map(self.map_to_price_ticker, json))
        return res

    def map_to_ticker_price_change_stat(self, json: BinanceTickerPriceChangeStatJson
                                        ) -> BinanceTickerPriceChangeStatModel:
        """Maps ticker price change statistics json
        to ticker price change statistics model.

        Args:
            json (BinanceTickerPriceChangeStatJson)

        Returns:
            BinanceTickerPriceChangeStatModel
        """

        res = BinanceTickerPriceChangeStatModel(
            symbol=json["symbol"],
            price_change=Decimal(json["priceChange"]),
            weighted_avg_price=Decimal(json["weightedAvgPrice"]),
            prev_close_price=Decimal(json["prevClosePrice"]),
            last_price=Decimal(json["lastPrice"]),
            last_qty=Decimal(json["lastQty"]),
            bid_price=Decimal(json["bidPrice"]),
            ask_price=Decimal(json["askPrice"]),
            open_price=Decimal(json["openPrice"]),
            high_price=Decimal(json["highPrice"]),
            low_price=Decimal(json["lowPrice"]),
            volume=Decimal(json["volume"]),
            quote_volume=Decimal(json["quoteVolume"]),
            open_time=json["openTime"],
            close_time=json["closeTime"],
            first_id=json["firstId"],
            last_id=json["lastId"],
            count=json["count"])
        return res

    def map_to_tickers_price_change_stat(self, json: BinanceTickersPriceChangeStatJson
                                         ) -> BinanceTickersPriceChangeStat:
        """Maps tickers price change statistics json
        to tickers price change statistics model.

        Args:
            json (BinanceTickersPriceChangeStatJson)

        Returns:
            BinanceTickersPriceChangeStat
        """

        res = list(map(self.map_to_ticker_price_change_stat, json))
        return res

    def map_to_trade(self, json: BinanceTradeJson) -> BinanceTradeModel:
        """Maps trade json to trade model.

        Args:
            json (BinanceTradeJson)

        Returns:
            BinanceTradeModel
        """

        res = BinanceTradeModel(
            id=json["id"],
            price=Decimal(json["price"]),
            qty=Decimal(json["qty"]),
            quote_qty=Decimal(json["quoteQty"]),
            time=json["time"],
            is_buyer_maker=json["isBuyerMaker"],
            is_best_match=json["isBestMatch"])
        return res

    def map_to_trades(self, json: BinanceTradesJson) -> BinanceTrades:
        """Maps trades json to trades model.

        Args:
            json (BinanceTradesJson)

        Returns:
            BinanceTrades
        """

        res = list(map(self.map_to_trade, json))
        return res

    def map_to_price_symbol_filter(self, json: BinancePriceSymbolFilterJson
                                   ) -> BinancePriceSymbolFilterModel:
        """Maps price symbol filter json to price symbol filter model.

        Args:
            json (BinancePriceSymbolFilterJson)

        Returns:
            BinancePriceSymbolFilterModel
        """

        res = BinancePriceSymbolFilterModel(
            filter_type=json["filterType"],
            min_price=Decimal(json["minPrice"]),
            max_price=Decimal(json["maxPrice"]),
            tick_size=Decimal(json["tickSize"]))
        return res

    def map_to_percent_price_symbol_filter(self, json: BinancePercentPriceSymbolFilterJson
                                           ) -> BinancePercentPriceSymbolFilterModel:
        """Maps percent price symbol filter json to percent price symbol filter model.

        Args:
            json (BinancePercentPriceSymbolFilterJson)

        Returns:
            BinancePercentPriceSymbolFilterModel
        """

        res = BinancePercentPriceSymbolFilterModel(
            filter_type=json["filterType"],
            multiplier_up=Decimal(json["multiplierUp"]),
            multiplier_down=Decimal(json["multiplierDown"]),
            avg_price_mins=json["avgPriceMins"])
        return res

    def map_to_lot_size_symbol_filter(self, json: BinanceLotSizeSymbolFilterJson
                                      ) -> BinanceLotSizeSymbolFilterModel:
        """Maps lot size symbol filter json to lot size symbol filter model.

        Args:
            json (BinanceLotSizeSymbolFilterJson)

        Returns:
            BinanceLotSizeSymbolFilterModel
        """

        res = BinanceLotSizeSymbolFilterModel(
            filter_type=json["filterType"],
            min_qty=Decimal(json["minQty"]),
            max_qty=Decimal(json["maxQty"]),
            step_size=Decimal(json["stepSize"]))
        return res

    def map_to_min_notional_symbol_filter(self, json: BinanceMinNotionalSymbolFilterJson
                                          ) -> BinanceMinNotionalSymbolFilterModel:
        """Maps min notional symbol filter json to min notional symbol filter model.

        Args:
            json (BinanceMinNotionalSymbolFilterJson)

        Returns:
            BinanceMinNotionalSymbolFilterModel
        """

        res = BinanceMinNotionalSymbolFilterModel(
            filter_type=json["filterType"],
            min_notional=Decimal(json["minNotional"]),
            apply_to_market=json["applyToMarket"],
            avg_price_mins=json["avgPriceMins"])
        return res

    def map_to_market_lot_size_symbol_filter(self, json: BinanceMarketLotSizeSymbolFilterJson
                                             ) -> BinanceMarketLotSizeSymbolFilterModel:
        """Maps market lot size symbol filter json to market lot size symbol filter model.

        Args:
            json (BinanceMarketLotSizeSymbolFilterJson)

        Returns:
            BinanceMarketLotSizeSymbolFilterModel
        """

        res = BinanceMarketLotSizeSymbolFilterModel(
            filter_type=json["filterType"],
            min_qty=Decimal(json["minQty"]),
            max_qty=Decimal(json["maxQty"]),
            step_size=Decimal(json["stepSize"]))
        return res

    def map_to_max_position_symbol_filter(self, json: BinanceMaxPositionSymbolFilterJson
                                          ) -> BinanceMaxPositionSymbolFilterModel:
        """Maps max position symbol filter json to max position symbol filter model.

        Args:
            json (BinanceMaxPositionSymbolFilterJson)

        Returns:
            BinanceMaxPositionSymbolFilterModel
        """

        res = BinanceMaxPositionSymbolFilterModel(
            filter_type=json["filterType"],
            max_position=Decimal(json["maxPosition"]))
        return res

    def map_to_iceberg_parts_symbol_filter(self, json: BinanceIcebergPartsSymbolFilterJson
                                           ) -> BinanceIcebergPartsSymbolFilterModel:
        """Maps iceberg parts symbol filter json to iceberg parts symbol filter model.

        Args:
            json (BinanceIcebergPartsSymbolFilterJson)

        Returns:
            BinanceIcebergPartsSymbolFilterModel
        """

        res = BinanceIcebergPartsSymbolFilterModel(
            filter_type=json["filterType"],
            limit=json["limit"])
        return res

    def map_to_max_num_orders_symbol_filter(self, json: BinanceMaxNumOrdersSymbolFilterJson
                                            ) -> BinanceMaxNumOrdersSymbolFilterModel:
        """Maps max num orders symbol filter json to max num orders symbol filter model.

        Args:
            json (BinanceMaxNumOrdersSymbolFilterJson)

        Returns:
            BinanceMaxNumOrdersSymbolFilterModel
        """

        res = BinanceMaxNumOrdersSymbolFilterModel(
            filter_type=json["filterType"],
            max_num_orders=json["maxNumOrders"])
        return res

    def map_to_max_num_algo_orders_symbol_filter(self, json: BinanceMaxNumAlgoOrdersSymbolFilterJson
                                                 ) -> BinanceMaxNumAlgoOrdersSymbolFilterModel:
        """Maps max num algo orders symbol filter json to max num algo orders symbol filter model.

        Args:
            json (BinanceMaxNumAlgoOrdersSymbolFilterJson)

        Returns:
            BinanceMaxNumAlgoOrdersSymbolFilterModel
        """

        res = BinanceMaxNumAlgoOrdersSymbolFilterModel(
            filter_type=json["filterType"],
            max_num_algo_orders=json["maxNumAlgoOrders"])
        return res

    def map_to_max_num_iceberg_orders_symbol_filter(
            self,
            json: BinanceMaxNumIcebergOrdersSymbolFilterJson
    ) -> BinanceMaxNumIcebergOrdersSymbolFilterModel:
        """Maps max num iceberg orders symbol filter json
        to max num iceberg orders symbol filter model.

        Args:
            json (BinanceMaxNumIcebergOrdersSymbolFilterJson)

        Returns:
            BinanceMaxNumIcebergOrdersSymbolFilterModel
        """

        res = BinanceMaxNumIcebergOrdersSymbolFilterModel(
            filter_type=json["filterType"],
            max_num_iceberg_orders=json["maxNumIcebergOrders"])
        return res

    def map_to_symbol_filter(self, json: BinanceSymbolFilterJson) -> BinanceSymbolFilterModel:
        """Maps symbol filter json to symbol filter model.

        Args:
            json (BinanceSymbolFilterJson)

        Returns:
            BinanceSymbolFilterModel
        """

        filter_type = json["filterType"]

        if filter_type == BinanceSymbolFilterType.PRICE:
            return self.map_to_price_symbol_filter(json)

        elif filter_type == BinanceSymbolFilterType.PERCENT_PRICE:
            return self.map_to_percent_price_symbol_filter(json)

        elif filter_type == BinanceSymbolFilterType.LOT_SIZE:
            return self.map_to_lot_size_symbol_filter(json)

        elif filter_type == BinanceSymbolFilterType.MIN_NOTIONAL:
            return self.map_to_min_notional_symbol_filter(json)

        elif filter_type == BinanceSymbolFilterType.MARKET_LOT_SIZE:
            return self.map_to_market_lot_size_symbol_filter(json)

        elif filter_type == BinanceSymbolFilterType.MAX_POSITION:
            return self.map_to_max_position_symbol_filter(json)

        elif filter_type == BinanceSymbolFilterType.ICEBERG_PARTS:
            return self.map_to_iceberg_parts_symbol_filter(json)

        elif filter_type == BinanceSymbolFilterType.MAX_NUM_ORDERS:
            return self.map_to_max_num_orders_symbol_filter(json)

        elif filter_type == BinanceSymbolFilterType.MAX_NUM_ALGO_ORDERS:
            return self.map_to_max_num_algo_orders_symbol_filter(json)

        elif filter_type == BinanceSymbolFilterType.MAX_NUM_ICEBERG_ORDERS:
            return self.map_to_max_num_iceberg_orders_symbol_filter(json)

        assert False, f"Unhandled symbol filter: {json}"

    def map_to_symbol_filters(self, json: BinanceSymbolFiltersJson) -> BinanceSymbolFilters:
        """Maps symbol filters json to symbol filters.

        Args:
            json (BinanceSymbolFiltersJson)

        Returns:
            BinanceSymbolFilters
        """

        res = list(map(self.map_to_symbol_filter, json))
        return res

    def map_to_symbol(self, json: BinanceSymbolJson) -> BinanceSymbolModel:
        """Maps symbol json to symbol model.

        Args:
            json (BinanceSymbolJson)

        Returns:
            BinanceSymbolModel
        """

        res = BinanceSymbolModel(
            symbol=json["symbol"],
            status=json["status"],
            base_asset=json["baseAsset"],
            base_asset_precision=json["baseAssetPrecision"],
            quote_asset=json["quoteAsset"],
            quote_precision=json["quotePrecision"],
            quote_asset_precision=json["quoteAssetPrecision"],
            order_types=json["orderTypes"],
            iceberg_allowed=json["icebergAllowed"],
            oco_allowed=json["ocoAllowed"],
            is_spot_trading_allowed=json["isSpotTradingAllowed"],
            is_margin_trading_allowed=json["isMarginTradingAllowed"],
            filters=self.map_to_symbol_filters(json["filters"]),
            permissions=json["permissions"])
        return res

    def map_to_symbols(self, json: BinanceSymbolsJson) -> BinanceSymbols:
        """Maps symbols json to symbols.

        Args:
            json (BinanceSymbolsJson)

        Returns:
            BinanceSymbols
        """

        res = list(map(self.map_to_symbol, json))
        return res

    def map_to_max_num_orders_exchange_filter(
            self,
            json: BinanceMaxNumOrdersExchangeFilterJson
    ) -> BinanceMaxNumOrdersExchangeFilterModel:
        """Maps max num orders exchnage filter json to
        max num orders exchange filter model.

        Args:
            json (BinanceMaxNumOrdersExchangeFilterJson)

        Returns:
            BinanceMaxNumOrdersExchangeFilterModel
        """

        res = BinanceMaxNumOrdersExchangeFilterModel(
            filter_type=json["filterType"],
            max_num_orders=json["maxNumOrders"])
        return res

    def map_to_max_num_algo_orders_exchange_filter(
            self,
            json: BinanceMaxNumAlgoOrdersExchangeFilterJson
    ) -> BinanceMaxNumAlgoOrdersExchangeFilterModel:
        """Maps max num algo orders exchnage filter json to
        max num algo orders exchange filter model.

        Args:
            json (BinanceMaxNumAlgoOrdersExchangeFilterJson)

        Returns:
            BinanceMaxNumAlgoOrdersExchangeFilterModel
        """

        res = BinanceMaxNumAlgoOrdersExchangeFilterModel(
            filter_type=json["filterType"],
            max_num_algo_orders=json["maxNumAlgoOrders"])
        return res

    def map_to_exchange_filter(self, json: BinanceExchangeFilterJson) -> BinanceExchangeFilterModel:
        """Maps exchange filter json to exchange filter model.

        Args:
            json (BinanceExchangeFilterJson)

        Returns:
            BinanceExchangeFilterModel
        """

        filter_type = json["filterType"]
        if filter_type == BinanceExchangeFilterType.MAX_NUM_ORDERS:
            return self.map_to_max_num_orders_exchange_filter(json)
        elif filter_type == BinanceExchangeFilterType.MAX_NUM_ALGO_ORDERS:
            return self.map_to_max_num_algo_orders_exchange_filter(json)

        assert False, f"Unhandled exchange filter: {json}"

    def map_to_exchange_filters(self, json: BinanceExchangeFiltersJson) -> BinanceExchangeFilters:
        """Maps exchange filters json to exchange filters model.

        Args:
            json (BinanceExchangeFilterJson)

        Returns:
            BinanceExchangeFilterModel
        """

        res = list(map(self.map_to_exchange_filter, json))
        return res

    def map_to_request_weight_rate_limit(self, json: BinanceRequestWeightRateLimitJson
                                         ) -> BinanceRequestWeightRateLimitModel:
        """Maps request weight rate limit json to request weight rate limit model.

        Args:
            json (BinanceRequestWeightRateLimitJson)

        Returns:
            BinanceRequestWeightRateLimitModel
        """

        res = BinanceRequestWeightRateLimitModel(
            rate_limit_type=json["rateLimitType"],
            interval=json["interval"],
            interval_num=json["intervalNum"],
            limit=json["limit"])
        return res

    def map_to_orders_rate_limit(self, json: BinanceOrdersRateLimitJson
                                 ) -> BinanceOrdersRateLimitModel:
        """Maps orders rate limit json to orders rate limit model.

        Args:
            json (BinanceOrdersRateLimitJson)

        Returns:
            BinanceOrdersRateLimitModel
        """

        res = BinanceOrdersRateLimitModel(
            rate_limit_type=json["rateLimitType"],
            interval=json["interval"],
            interval_num=json["intervalNum"],
            limit=json["limit"])
        return res

    def map_to_raw_requests_rate_limit(self, json: BinanceRawRequestsRateLimitJson
                                       ) -> BinanceRawRequestsRateLimitModel:
        """Maps raw requests rate limit json to raw requests rate limit model.

        Args:
            json (BinanceRawRequestsRateLimitJson)

        Returns:
            BinanceRawRequestsRateLimitModel
        """

        res = BinanceRawRequestsRateLimitModel(
            rate_limit_type=json["rateLimitType"],
            interval=json["interval"],
            interval_num=json["intervalNum"],
            limit=json["limit"])
        return res

    def map_to_rate_limit(self, json: BinanceRateLimitJson) -> BinanceRateLimitModel:
        """Maps rate limit json to rate limit model.

        Args:
            json (BinanceRateLimitJson)

        Returns:
            BinanceRateLimitModel
        """

        rate_limit_type = json["rateLimitType"]

        if rate_limit_type == BinanceRateLimitType.REQUEST_WEIGHT:
            return self.map_to_request_weight_rate_limit(json)
        elif rate_limit_type == BinanceRateLimitType.ORDERS:
            return self.map_to_orders_rate_limit(json)
        elif rate_limit_type == BinanceRateLimitType.RAW_REQUESTS:
            return self.map_to_raw_requests_rate_limit(json)

    def map_to_rate_limits(self, json: BinanceRateLimitsJson) -> BinanceRateLimits:
        """Maps rate limits json to rate limits model.

        Args:
            json (BinanceRateLimitsJson)

        Returns:
            BinanceRateLimits
        """

        res = list(map(self.map_to_rate_limit, json))
        return res

    def map_to_exchange_info(self, json: BinanceExchangeInfoJson) -> BinanceExchangeInfoModel:
        """Maps exchange info json to exchange info model.

        Args:
            json (BinanceExchangeInfoJson)

        Returns:
            BinanceExchangeInfoModel
        """

        res = BinanceExchangeInfoModel(
            timezone=json["timezone"],
            server_time=json["serverTime"],
            rate_limits=self.map_to_rate_limits(json["rateLimits"]),
            exchange_filters=self.map_to_exchange_filters(
                json["exchangeFilters"]),
            symbols=self.map_to_symbols(json["symbols"]))
        return res

    def map_to_balance(self, json: BinanceCurrencyBalanceJson) -> BinanceCurrencyBalanceModel:
        """Maps balance json to balance model.

        Args:
            json (BinanceCurrencyBalanceJson)

        Returns:
            BinanceCurrencyBalanceModel
        """

        res = BinanceCurrencyBalanceModel(
            asset=json["asset"],
            free=Decimal(json["free"]),
            locked=Decimal(json["locked"]))
        return res

    def map_to_balances(self, json: BinanceCurrencyBalancesJson) -> BinanceCurrencyBalances:
        """Maps balances json to balances model.

        Args:
            json (BinanceCurrencyBalancesJson)

        Returns:
            BinanceCurrencyBalances
        """

        res = list(map(self.map_to_balance, json))
        return res

    def map_to_account_info(self, json: BinanceAccountInfoJson) -> BinanceAccountInfoModel:
        """Maps account info json to account info model.

        Args:
            json (BinanceAccountInfoJson)

        Returns:
            BinanceAccountInfoModel
        """

        res = BinanceAccountInfoModel(
            maker_commission=json["makerCommission"],
            taker_commission=json["takerCommission"],
            buyer_commission=json["buyerCommission"],
            seller_commission=json["sellerCommission"],
            can_trade=json["canTrade"],
            can_withdraw=json["canWithdraw"],
            can_deposit=json["canDeposit"],
            update_time=json["updateTime"],
            account_type=json["accountType"],
            balances=self.map_to_balances(json["balances"]))
        return res
