from abc import ABC, abstractmethod

__all__ = [
    'Downloader'
]


class Downloader(ABC):
    """
    Abstract Downloader class as a skeleton for particular markets implementations.
    """

    @abstractmethod
    def check_exchange_availability(self):
        """Check if current exchange is available"""
        raise NotImplementedError()

    @abstractmethod
    async def check_exchange_availability_async(self):
        """Check if current exchange is available (async)"""
        raise NotImplementedError()

    @abstractmethod
    def download_trades(self, *args, **kwargs):
        """
        Download trades.
        """
        raise NotImplementedError()

    @abstractmethod
    async def download_trades_async(self, *args, **kwargs):
        """
        Download trades. (async)
        """
        raise NotImplementedError()

    @abstractmethod
    def download_candles(self, *args, **kwargs):
        """
        Download candles.
        """
        raise NotImplementedError()

    @abstractmethod
    async def download_candles_async(self, *args, **kwargs):
        """
        Download candles. (async)
        """
        raise NotImplementedError()

    @abstractmethod
    def download_order_books(self, *args, **kwargs):
        """
        Download order books.
        """
        raise NotImplementedError()

    @abstractmethod
    async def download_order_books_async(self, *args, **kwargs):
        """
        Download order books. (async)
        """
        raise NotImplementedError()
