import requests

from agoda.config.config import Config
from agoda.downloader import DownloaderIF, URL


class HTTPDownloader(DownloaderIF):
    def __init__(self):
        self.configs = Config()

    def authenticate(self, url: URL) -> bool:
        pass

    def download(self, url, dest_path):
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(dest_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=self.configs.get('downloader')['chunk_size']):
                    f.write(chunk)

        return dest_path
