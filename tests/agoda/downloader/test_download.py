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
                'ftp://speedtest.tele2.net/512KB.zip',
                'ftp://anonymous:anonymous@speedtest.tele2.net/1MB.zip']
        dest_urls = self.download.download_urls(urls)
        for url, dest in zip(urls, dest_urls):
            print("Downloading:", url)
            self.assertTrue(os.path.exists(dest))
            print("-> Passed:", dest)


if __name__ == '__main__':
    unittest.main()
