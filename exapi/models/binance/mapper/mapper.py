"""Has binance models mapper interface."""

from decimal import Decimal

from exapi.models.binance import (BinanceAveragePriceJson,
                                  BinanceAveragePriceModel, BinanceCandleJson,
                                  BinanceCandleModel, BinanceCandles,
                                  BinanceCandlesJson, BinanceFilledOrderJson,
                                  BinanceFilledOrderModel, BinanceFilledOrders,
                                  BinanceFilledOrdersJson,
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
                                  BinancePingJson, BinancePingModel,
                                  BinancePriceTickerJson,
                                  BinancePriceTickerModel, BinancePriceTickers,
                                  BinancePriceTickersJson,
                                  BinanceServerTimeJson,
                                  BinanceServerTimeModel,
                                  BinanceTickerPriceChangeStatJson,
                                  BinanceTickerPriceChangeStatModel,
                                  BinanceTickersPriceChangeStat,
                                  BinanceTickersPriceChangeStatJson,
                                  BinanceTradeJson, BinanceTradeModel,
                                  BinanceTrades, BinanceTradesJson)


class BinanceModelsMapper:
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
