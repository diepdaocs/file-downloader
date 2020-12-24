import os
import unittest

from agoda.downloader.download import Download


class DownloadTestCase(unittest.TestCase):
    def setUp(self):
        self.dest_path = 'tests/data'
        self.download = Download(self.dest_path)

    def test_download_urls(self):
        urls = ['https://www.facebook.com/favicon.ico',
                'https://www.google.com/favicon.ico',
                'http://ovh.net/files/1Mb.dat']
        urls = self.download.download_urls(urls)
        for url in urls:
            self.assertTrue(os.path.exists(url))


if __name__ == '__main__':
    unittest.main()
