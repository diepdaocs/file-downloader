import logging
import os
import re
from multiprocessing.dummy import Pool

from file_downloader.downloader.downloader_factory import DownloaderFactory
from file_downloader.downloader.exceptions import DownloadException, UnsupportedProtocolException, \
    MissingProtocolException


class Download(object):
    def __init__(self, dest_path, downloader_factory=None):
        self.dest_path = dest_path
        self.downloader_factory = downloader_factory or DownloaderFactory()
        self.logger = logging.getLogger(self.__class__.__name__)

    @staticmethod
    def _build_filename(url) -> str:
        return re.sub(r'[:/]', '-', url)

    def download(self, url, refresh=False):
        self.logger.info('Downloading url: %s', url)
        filename = self._build_filename(url)
        dest_path = os.path.join(self.dest_path, filename)
        if not refresh and os.path.exists(dest_path):
            self.logger.info('File existed, skip!!! %s', dest_path)
            return dest_path
        try:
            downloader = self.downloader_factory.get(url)
            downloader.download_url(url, dest_path)
            self.logger.info('Downloaded to: %s', dest_path)
        except DownloadException as e:
            self.logger.exception(e.message)
            os.remove(dest_path)
            self.logger.info('Removed incomplete file: %s', dest_path)
        except (UnsupportedProtocolException, MissingProtocolException) as e:
            self.logger.exception(e.message)

        return dest_path

    def download_wrapper(self, args):
        return self.download(*args)

    def download_urls(self, urls, refresh=False):
        pool = Pool()
        results = pool.map(self.download_wrapper, [(url, refresh) for url in urls])
        pool.close()
        return results
