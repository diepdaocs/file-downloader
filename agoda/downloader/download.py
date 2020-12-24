import os
import re

from agoda.downloader.downloader_factory import DownloaderFactory


class Download(object):
    def __init__(self, dest_path):
        self.dest_path = dest_path
        self.downloader_factory = DownloaderFactory()

    @staticmethod
    def _build_filename(url) -> str:
        return re.sub(r'[:/]', '-', url)

    def download(self, url):
        filename = self._build_filename(url)
        dest_path = os.path.join(self.dest_path, filename)
        if os.path.exists(dest_path):
            return dest_path

        downloader = self.downloader_factory.get(url)
        return downloader.download(url, dest_path)

    def download_urls(self, urls):
        ret = []
        for url in urls:
            ret.append(self.download(url))
        return ret
