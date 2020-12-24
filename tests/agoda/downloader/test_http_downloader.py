import os
import unittest

from agoda.downloader.http_downloader import HTTPDownloader


class HTTPDownloaderTestCase(unittest.TestCase):
    def setUp(self):
        self.dest_path = 'tests/data'
        self.downloader = HTTPDownloader()

    def test_download_urls(self):
        urls = ['https://www.facebook.com/favicon.ico',
                'https://www.google.com/favicon.ico']
        dest_urls = [self.downloader.download(url, self.dest_path) for url in urls]
        for url, dest in zip(urls, dest_urls):
            print("Downloading:", url)
            self.assertTrue(os.path.exists(dest))
            print("-> Passed:", dest)


if __name__ == '__main__':
    unittest.main()
