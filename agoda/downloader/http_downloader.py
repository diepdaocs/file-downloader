import requests

from agoda.downloader import DownloaderIF, URL


class HTTPDownloader(DownloaderIF):

    def authenticate(self, url: URL) -> bool:
        pass

    def download(self, url, dest_path):
        with open(dest_path, 'wb') as f:
            r = requests.get(url, allow_redirects=True)
            f.write(r.content)

        return dest_path
