from typing import Protocol, Optional


class IBinanceSpotMarketDataChannelCreator(Protocol):
    """Binance spot market data socket channel creator."""

    def create_agg_trades_channel(self, symbol: str) -> str:
        """Creates agg trade channel.

        Args:
            symbol (str)

        Returns:
            str
        """

    def create_trades_channel(self, symbol: str) -> str:
        """Creates trade channel.

        Args:
            symbol (str)

        Returns:
            str
        """

    def create_candles_channel(self, symbol: str) -> str:
        """Creates candles channel.

        Args:
            symbol (str)

        Returns:
            str
        """

    def create_mini_ticker_channel(self, symbol: str) -> str:
        """Creates symbol mini ticker channel.

        Args:
            symbol (str)

        Returns:
            str
        """

    def create_mini_tickers_channel(self) -> str:
        """Creates all symbol mini tickers channel.

        Returns:
            str
        """

    def create_ticker_channel(self, symbol: str) -> str:
        """Creates individual symbol ticker channel.

        Args:
            symbol (str)

        Returns:
            str
        """

    def create_tickers_channel(self) -> str:
        """Creates all symbol tickers channel.

        Args:
            symbol (str)

        Returns:
            str
        """

    def create_book_ticker_channel(self, symbol: str) -> str:
        """Creates symbol book ticker channel.

        Args:
            symbol (str)

        Returns:
            str
        """

    def create_book_tickers_channel(self) -> str:
        """Creates all symbol book tickers channel.

        Returns:
            str
        """

    def create_order_book_channel(self, symbol: str,
                                  levels: Optional[int] = None,
                                  update_speed: Optional[int] = None) -> str:
        """Creates depth channel.

        Args:
            symbol (str)
            levels (Optional[int]): count of bid and ask orders.
            update_speed (Optional[int])

        Returns:
            str
        """
