from agoda.downloader import DownloaderIF
from agoda.downloader.ftp_downloader import FTPDownloader
from agoda.downloader.http_downloader import HTTPDownloader


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
        if url.startswith('http'):
            return self.http_downloader
        elif url.startswith('ftp'):
            return self.ftp_downloader
