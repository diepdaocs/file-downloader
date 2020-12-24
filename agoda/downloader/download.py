from agoda.downloader.downloader_factory import DownloaderFactory


class Download(object):
    def __init__(self, dest_path):
        self.dest_path = dest_path
        self.downloader_factory = DownloaderFactory()

    def download(self, url):
        downloader = self.downloader_factory.get(url)
        return downloader.download(url, self.dest_path)

    def download_urls(self, urls):
        ret = []
        for url in urls:
            ret.append(self.download(url))
        return ret
