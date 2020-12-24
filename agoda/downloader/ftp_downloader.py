from agoda.downloader import DownloaderIF, URL


class FTPDownloader(DownloaderIF):
    def authenticate(self, url: URL) -> bool:
        pass

    def download(self, url, dest_path):
        pass
