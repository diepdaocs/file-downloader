import os

import requests

from agoda.downloader import DownloaderIF, URL


class HTTPDownloader(DownloaderIF):

    def authenticate(self, url: URL) -> bool:
        pass

    def download(self, url, dest_path):
        file_name = self.build_filename(url)
        file_path = os.path.join(dest_path, file_name)
        with open(file_path, 'wb') as f:
            r = requests.get(url, allow_redirects=True)
            f.write(r.content)

        return file_path
