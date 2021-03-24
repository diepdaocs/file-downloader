from file_downloader.downloader import DownloaderIF
from file_downloader.downloader.exceptions import UnsupportedProtocolException, MissingProtocolException
from file_downloader.downloader.ftp_downloader import FTPDownloader
from file_downloader.downloader.http_downloader import HTTPDownloader


class DownloaderFactory(object):
    """
    To build and select appropriate downloader
        - downloader are lazy initiated by the property annotation
    """

    @property
    def ftp_downloader(self):
        return FTPDownloader()

    @property
    def http_downloader(self):
        return HTTPDownloader()

    def get(self, url) -> DownloaderIF:
        if ':' not in url:
            raise MissingProtocolException(url)
        if url.startswith('http'):
            return self.http_downloader
        elif url.startswith('ftp'):
            return self.ftp_downloader
        else:
            raise UnsupportedProtocolException(url)
