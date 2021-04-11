"""Has hitbtc models mapper interface."""

from decimal import Decimal

from exapi.models.hitbtc import (HitbtcCandleModel, HitbtcCandles, HitbtcCurrencies, HitbtcCurrencyModel,
                                 HitbtcOrderBookModel, HitbtcOrderBookOrderModel, HitbtcOrderBooks, HitbtcOrderModel,
                                 HitbtcOrders, HitbtcRawCandleModel, HitbtcRawCandles, HitbtcRawCurrencies,
                                 HitbtcRawCurrencyModel, HitbtcRawOrderBookModel, HitbtcRawOrderBookOrderModel,
                                 HitbtcRawOrderBooks, HitbtcRawOrderModel, HitbtcRawOrders, HitbtcRawSymbolCandles,
                                 HitbtcRawSymbolModel, HitbtcRawSymbolTrades, HitbtcRawSymbols, HitbtcRawTickerModel,
                                 HitbtcRawTickers, HitbtcRawTradeModel, HitbtcRawTrades,
                                 HitbtcRawTradingCurrencyBalanceModel, HitbtcRawTradingCurrencyBalances,
                                 HitbtcRawTradingFeeModel, HitbtcSymbolCandles, HitbtcSymbolModel, HitbtcSymbolTrades,
                                 HitbtcSymbols, HitbtcTickerModel, HitbtcTickers, HitbtcTradeModel, HitbtcTrades,
                                 HitbtcTradingCurrencyBalanceModel, HitbtcTradingCurrencyBalances,
                                 HitbtcTradingFeeModel)
from exapi.models.hitbtc.mapper.base import HitbtcBaseModelsMapper


class HitbtcModelsMapper(HitbtcBaseModelsMapper):
    """Hitbtc models mapper.

    Has methods for mapping hitbtc json models to hitbtc dataclass models.
    """

    def map_to_currency(self, raw_currency: HitbtcRawCurrencyModel) -> HitbtcCurrencyModel:
        """Maps currency json to currency model.

        Args:
            raw_currency (HitbtcRawCurrency)

        Returns:
            HitbtcCurrencyModel
        """

        id_ = raw_currency["id"]
        full_name = raw_currency["fullName"]
        crypto = raw_currency["crypto"]
        payin_enabled = raw_currency["payinEnabled"]
        payin_payment_id = raw_currency["payinPaymentId"]
        payin_confirmations = raw_currency["payinConfirmations"]
        payout_enabled = raw_currency["payoutEnabled"]
        payout_is_payment_id = raw_currency["payoutIsPaymentId"]
        transfer_enabled = raw_currency["transferEnabled"]
        delisted = raw_currency["delisted"]
        precision_payout = int(raw_currency["precisionPayout"])
        precision_transfer = int(raw_currency["precisionTransfer"])
        raw_payout_fee = raw_currency.get("payoutFee")
        payout_fee = Decimal(
            raw_payout_fee) if raw_payout_fee is not None else raw_payout_fee

        currency = HitbtcCurrencyModel(
            id=id_,
            full_name=full_name,
            crypto=crypto,
            payin_enabled=payin_enabled,
            payin_payment_id=payin_payment_id,
            payin_confirmations=payin_confirmations,
            payout_enabled=payout_enabled,
            payout_is_payment_id=payout_is_payment_id,
            transfer_enabled=transfer_enabled,
            delisted=delisted,
            payout_fee=payout_fee,
            precision_payout=precision_payout,
            precision_transfer=precision_transfer)

        return currency

    def map_to_currencies(self, raw_currencies: HitbtcRawCurrencies) -> HitbtcCurrencies:
        """Maps currencies json to currencies model.

        Args:
            raw_currencies (HitbtcRawCurrencies)

        Returns:
            HitbtcCurrencies
        """

        currencies = list(map(self.map_to_currency, raw_currencies))
        return currencies

    def map_to_symbol(self, raw_symbol: HitbtcRawSymbolModel) -> HitbtcSymbolModel:
        """Maps symbol json to symbol model.

        Args:
            raw_symbol (HitbtcRawSymbol)

        Returns:
            HitbtcSymbolModel
        """

        id_ = raw_symbol["id"]
        base_currency = raw_symbol["baseCurrency"]
        quote_currency = raw_symbol["quoteCurrency"]
        quantity_increment = Decimal(raw_symbol["quantityIncrement"])
        tick_size = Decimal(raw_symbol["tickSize"])
        take_liquidity_rate = Decimal(raw_symbol["takeLiquidityRate"])
        provide_liquidity_rate = Decimal(raw_symbol["provideLiquidityRate"])
        fee_currency = raw_symbol["feeCurrency"]

        symbol = HitbtcSymbolModel(
            id=id_,
            base_currency=base_currency,
            quote_currency=quote_currency,
            quantity_increment=quantity_increment,
            tick_size=tick_size,
            take_liquidity_rate=take_liquidity_rate,
            provide_liquidity_rate=provide_liquidity_rate,
            fee_currency=fee_currency)

        return symbol

    def map_to_symbols(self, raw_symbols: HitbtcRawSymbols) -> HitbtcSymbols:
        """Maps symbols json to symbols model.

        Args:
            raw_symbols (HitbtcRawSymbols)

        Returns:
            HitbtcSymbols
        """

        symbols = list(map(self.map_to_symbol, raw_symbols))
        return symbols

    def map_to_orderbook_order(self, raw_orderbook_order: HitbtcRawOrderBookOrderModel
                               ) -> HitbtcOrderBookOrderModel:
        """Maps orderbook order json to orderbook order model.

        Args:
            raw_orderbook_order (HitbtcRawOrderBookOrder)

        Returns:
            HitbtcOrderBookOrder
        """

        price = Decimal(raw_orderbook_order["price"])
        size = Decimal(raw_orderbook_order["size"])
        order = HitbtcOrderBookOrderModel(price=price, size=size)
        return order

    def map_to_orderbook(self, raw_orderbook: HitbtcRawOrderBookModel
                         ) -> HitbtcOrderBookModel:
        """Maps orderbook json to orderbook model.

        Args:
            raw_orderbook (HitbtcRawOrderBookModel)

        Returns:
            HitbtcOrderBookModel
        """

        ask = list(map(self.map_to_orderbook_order, raw_orderbook["ask"]))
        bid = list(map(self.map_to_orderbook_order, raw_orderbook["bid"]))
        timestamp = raw_orderbook["timestamp"]
        symbol = raw_orderbook["symbol"]

        orderbook = HitbtcOrderBookModel(
            ask=ask, bid=bid, timestamp=timestamp, symbol=symbol)
        return orderbook

    def map_to_orderbooks(self, raw_orderbooks: HitbtcRawOrderBooks) -> HitbtcOrderBooks:
        """Maps orderbooks json to orderbooks model.

        Args:
            raw_orderbook (HitbtcRawOrderBooks)

        Returns:
            HitbtcOrderBooks
        """

        orderbooks: HitbtcOrderBooks = {}
        for symbol, raw_orderbook in raw_orderbooks.items():
            orderbooks[symbol] = self.map_to_orderbook(raw_orderbook)
        return orderbooks

    def map_to_ticker(self, raw_ticker: HitbtcRawTickerModel) -> HitbtcTickerModel:
        """Maps ticker json to ticker model.

        Args:
            raw_ticker (HitbtcRawTicker)

        Returns:
            HitbtcTickerModel
        """

        symbol = raw_ticker["symbol"]
        low = Decimal(raw_ticker["low"])
        high = Decimal(raw_ticker["high"])
        volume = Decimal(raw_ticker["volume"])
        volume_quote = Decimal(raw_ticker["volumeQuote"])
        timestamp = raw_ticker["timestamp"]
        raw_ask = raw_ticker["ask"]
        ask = Decimal(raw_ask) if raw_ask is not None else raw_ask
        raw_bid = raw_ticker["bid"]
        bid = Decimal(raw_bid) if raw_bid is not None else raw_bid
        raw_last = raw_ticker["last"]
        last = Decimal(raw_last) if raw_last is not None else raw_last
        raw_open = raw_ticker["open"]
        open_ = Decimal(raw_open) if raw_open is not None else raw_open

        ticker = HitbtcTickerModel(
            symbol=symbol,
            low=low,
            high=high,
            volume=volume,
            volume_quote=volume_quote,
            timestamp=timestamp,
            ask=ask,
            bid=bid,
            last=last,
            open=open_)

        return ticker

    def map_to_tickers(self, raw_tickers: HitbtcRawTickers) -> HitbtcTickers:
        """Maps tickers json to tickers model.

        Args:
            raw_ticker (HitbtcRawTickers)

        Returns:
            HitbtcTickers
        """

        tickers = list(map(self.map_to_ticker, raw_tickers))
        return tickers

    def map_to_trade(self, raw_trade: HitbtcRawTradeModel) -> HitbtcTradeModel:
        """Maps trade json to trade model.

        Args:
            raw_trade (HitbtcRawTradeModel)

        Returns:
            HitbtcTradeModel
        """

        id_ = int(raw_trade["id"])
        price = Decimal(raw_trade["price"])
        quantity = Decimal(raw_trade["quantity"])
        side = raw_trade["side"]
        timestamp = raw_trade["timestamp"]

        trade = HitbtcTradeModel(
            id=id_,
            price=price,
            quantity=quantity,
            side=side,
            timestamp=timestamp)

        return trade

    def map_to_trades(self, raw_trades: HitbtcRawTrades) -> HitbtcTrades:
        """Maps trades json to trades.

        Args:
            raw_trades (HitbtcRawTrades)

        Returns:
            HitbtcTrades
        """

        trades: HitbtcTrades = {}
        for symbol, raw_symbol_trades in raw_trades.items():
            trades[symbol] = self.map_to_symbol_trades(raw_symbol_trades)
        return trades

    def map_to_symbol_trades(self, raw_trades: HitbtcRawSymbolTrades) -> HitbtcSymbolTrades:
        """Maps symbol trades json to symbol trades model.

        Args:
            raw_trades (HitbtcRawTrade)

        Returns:
            HitbtcSymbolTrades
        """

        trades = list(map(self.map_to_trade, raw_trades))
        return trades

    def map_to_candle(self, raw_candle: HitbtcRawCandleModel) -> HitbtcCandleModel:
        """Maps candle json to candle.

        Args:
            raw_candle (HitbtcRawCandle)

        Returns:
            HitbtcCandleModel
        """

        timestamp = raw_candle["timestamp"]
        open_ = Decimal(raw_candle["open"])
        close = Decimal(raw_candle["close"])
        min_ = Decimal(raw_candle["min"])
        max_ = Decimal(raw_candle["max"])
        volume = Decimal(raw_candle["volume"])
        volume_quote = Decimal(raw_candle["volumeQuote"])

        candle = HitbtcCandleModel(
            timestamp=timestamp,
            open=open_,
            close=close,
            min=min_,
            max=max_,
            volume=volume,
            volume_quote=volume_quote)

        return candle

    def map_to_candles(self, raw_candles: HitbtcRawCandles) -> HitbtcCandles:
        """Maps candles json to candles.

        Args:
            raw_candles (HitbtcRawCandles)

        Returns:
            HitbtcCandles
        """

        candles: HitbtcCandles = {}
        for symbol, raw_symbol_candles in raw_candles.items():
            candles[symbol] = self.map_to_symbol_candles(raw_symbol_candles)
        return candles

    def map_to_symbol_candles(self, raw_candles: HitbtcRawSymbolCandles) -> HitbtcSymbolCandles:
        """Maps symbol candles json to symbol candles model.

        Args:
            raw_candles (HitbtcRawTrade)

        Returns:
            HitbtcSymbolCandles
        """

        candles = list(map(self.map_to_candle, raw_candles))
        return candles

    def map_to_order(self, raw_order: HitbtcRawOrderModel) -> HitbtcOrderModel:
        """Maps order json to order model.

        Args:
            raw_order (HitbtcRawOrderModel)

        Returns:
            HitbtcOrderModel
        """

        id_ = raw_order["id"]
        client_order_id = raw_order["clientOrderId"]
        symbol = raw_order["symbol"]
        side = raw_order["side"]
        status = raw_order["status"]
        type_ = raw_order["type"]
        time_in_force = raw_order["timeInForce"]
        quantity = Decimal(raw_order["quantity"])
        price = Decimal(raw_order["price"])
        cum_quantity = Decimal(raw_order["cumQuantity"])
        created_at = raw_order["createdAt"]
        updated_at = raw_order["updatedAt"]
        post_only = raw_order["postOnly"]
        raw_avg_price = raw_order.get("avgPrice")
        avg_price = Decimal(
            raw_avg_price) if raw_avg_price is not None else raw_avg_price
        raw_stop_price = raw_order.get("stopPrice")
        stop_price = Decimal(
            raw_stop_price) if raw_stop_price is not None else raw_stop_price
        expire_time = raw_order.get("expireTime")
        raw_trades_report = raw_order.get("tradesReport")
        trades_report = (self.map_to_symbol_trades(
            raw_trades_report) if raw_trades_report is not None else raw_trades_report)

        res = HitbtcOrderModel(
            id=id_,
            client_order_id=client_order_id,
            symbol=symbol,
            side=side,
            status=status,
            type=type_,
            time_in_force=time_in_force,
            quantity=quantity,
            price=price,
            cum_quantity=cum_quantity,
            created_at=created_at,
            updated_at=updated_at,
            post_only=post_only,
            avg_price=avg_price,
            stop_price=stop_price,
            expire_time=expire_time,
            trades_report=trades_report)

        return res

    def map_to_orders(self, raw_orders: HitbtcRawOrders) -> HitbtcOrders:
        """Maps orders json to list of order.

        Args:
            raw_orders (HitbtcRawOrders)

        Returns:
            HitbtcOrders
        """

        res = list(map(self.map_to_order, raw_orders))
        return res

    def map_to_trading_currency_balance(self, raw_balance: HitbtcRawTradingCurrencyBalanceModel
                                        ) -> HitbtcTradingCurrencyBalanceModel:
        """Maps trading currency balance json to trading currency balance.

        Args:
            raw_balance (HitbtcRawTradingCurrencyBalanceModel)

        Returns:
            HitbtcTradingCurrencyBalanceModel
        """

        currency = raw_balance["currency"]
        available = Decimal(raw_balance["available"])
        reserved = Decimal(raw_balance["reserved"])
        res = HitbtcTradingCurrencyBalanceModel(
            currency=currency,
            available=available,
            reserved=reserved)
        return res

    def map_to_trading_balance(self, raw_balance: HitbtcRawTradingCurrencyBalances
                               ) -> HitbtcTradingCurrencyBalances:
        """Maps trading balance json to trading balance.

        Args:
            raw_balance (HitbtcRawTradingCurrencyBalances)

        Returns:
            HitbtcTradingCurrencyBalances
        """

        res = list(map(self.map_to_trading_currency_balance, raw_balance))
        return res

    def map_to_trading_fee(self, raw_fee: HitbtcRawTradingFeeModel) -> HitbtcTradingFeeModel:
        """Maps orders json to list of order.

        Args:
            raw_orders (HitbtcRawOrders)

        Returns:
            HitbtcOrders
        """

        take_liquidity_rate = Decimal(raw_fee["takeLiquidityRate"])
        provide_liquidity_rate = Decimal(raw_fee["provideLiquidityRate"])
        res = HitbtcTradingFeeModel(
            take_liquidity_rate=take_liquidity_rate,
            provide_liquidity_rate=provide_liquidity_rate)
        return res
