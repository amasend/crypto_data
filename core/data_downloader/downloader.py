from abc import abstractmethod
from typing import TYPE_CHECKING

from .base_downloader import Downloader

if TYPE_CHECKING:
    from datetime import datetime
    from core.containers import Trades, Candles, OrderBooks

__all__ = [
    'HistoricalDownloader',
    'RealTimeDownloader'
]


class HistoricalDownloader(Downloader):
    """
    Base Downloader class as a skeleton for particular markets implementations (Historical Data)
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
    def download_trades(self, start_date: 'datetime', end_date: 'datetime' = None) -> 'Trades':
        """
        Download trades from specific date till specific date, If end_date is None, it indicates to
        download till current time.

        Parameters
        ----------
        start_date: datetime.datetime, required

        end_date: datetime.datetime, optional

        Returns
        -------
        Trades - specific container for better trades manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    async def download_trades_async(self, start_date: 'datetime', end_date: 'datetime' = None) -> 'Trades':
        """
        Download trades from specific date till specific date, If end_date is None, it indicates to
        download till current time. (async)

        Parameters
        ----------
        start_date: datetime.datetime, required

        end_date: datetime.datetime, optional

        Returns
        -------
        Trades - specific container for better trades manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    def download_candles(self, start_date: 'datetime', end_date: 'datetime' = None) -> 'Candles':
        """
        Download candles from specific date till specific date, If end_date is None, it indicates to
        download till current time.

        Parameters
        ----------
        start_date: datetime.datetime, required

        end_date: datetime.datetime, optional

        Returns
        -------
        Candles - specific container for better trades manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    async def download_candles_async(self, start_date: 'datetime', end_date: 'datetime' = None) -> 'Candles':
        """
        Download candles from specific date till specific date, If end_date is None, it indicates to
        download till current time. (async)

        Parameters
        ----------
        start_date: datetime.datetime, required

        end_date: datetime.datetime, optional

        Returns
        -------
        Candles - specific container for better trades manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    def download_order_books(self, start_date: 'datetime', end_date: 'datetime' = None) -> 'OrderBooks':
        """
        Download order books from specific date till specific date, If end_date is None, it indicates to
        download till current time.

        Parameters
        ----------
        start_date: datetime.datetime, required

        end_date: datetime.datetime, optional

        Returns
        -------
        OrderBooks - specific container for better trades manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    async def download_order_books_async(self, start_date: 'datetime',
                                         end_date: 'datetime' = None) -> 'OrderBooks':
        """
        Download order books from specific date till specific date, If end_date is None, it indicates to
        download till current time. (async)

        Parameters
        ----------
        start_date: datetime.datetime, required

        end_date: datetime.datetime, optional

        Returns
        -------
        OrderBooks - specific container for better trades manipulation.
        """
        raise NotImplementedError()


class RealTimeDownloader(Downloader):
    """
    Base Downloader class as a skeleton for particular markets implementations (Real Time Data)
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
    def download_trades(self) -> 'Trades':
        """
        Download trades starting from now.

        Returns
        -------
        Trades - specific container for better trades manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    async def download_trades_async(self) -> 'Trades':
        """
        Download trades starting from now. (async)

        Returns
        -------
        Trades - specific container for better trades manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    def download_candles(self) -> 'Candles':
        """
        Download candles.

        Returns
        -------
        Candles - specific container for better candles manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    async def download_candles_async(self) -> 'Candles':
        """
        Download candles. (async)

        Returns
        -------
        Candles - specific container for better candles manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    def download_order_books(self) -> 'OrderBooks':
        """
        Download order books.

        Returns
        -------
        OrderBooks - specific container for better order books manipulation.
        """
        raise NotImplementedError()

    @abstractmethod
    async def download_order_books_async(self) -> 'OrderBooks':
        """
        Download order books. (async)

        Returns
        -------
        OrderBooks - specific container for better order books manipulation.
        """
        raise NotImplementedError()
