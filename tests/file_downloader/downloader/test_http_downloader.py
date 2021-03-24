import os
import unittest

from file_downloader.downloader.download import Download
from file_downloader.downloader.http_downloader import HTTPDownloader


class HTTPDownloaderTestCase(unittest.TestCase):
    def setUp(self):
        self.dest_path = 'tests/data'
        self.downloader = HTTPDownloader()

    def _build_dest_path(self, url):
        return os.path.join(self.dest_path, Download._build_filename(url))

    def test_download_urls(self):
        urls = ['https://www.facebook.com/favicon.ico',
                'https://www.google.com/favicon.ico']
        dest_urls = [self.downloader.download(url, self._build_dest_path(url)) for url in urls]
        for url, dest in zip(urls, dest_urls):
            print("Downloading:", url)
            self.assertTrue(os.path.exists(dest))
            print("-> Passed:", dest)


if __name__ == '__main__':
    unittest.main()
