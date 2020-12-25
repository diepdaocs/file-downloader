import os
import unittest

from agoda.downloader.download import Download
from agoda.downloader.ftp_downloader import FTPDownloader


class FTPDownloaderTestCase(unittest.TestCase):
    def setUp(self):
        self.dest_path = 'tests/data'
        self.downloader = FTPDownloader()

    def _build_dest_path(self, url):
        return os.path.join(self.dest_path, Download._build_filename(url))

    def test_download_urls(self):
        urls = [
            'ftp://speedtest.tele2.net/512KB.zip',
            'ftp://anonymous:anonymous@speedtest.tele2.net/1MB.zip'
        ]
        dest_urls = [self.downloader.download(url, self._build_dest_path(url)) for url in urls]
        for url, dest in zip(urls, dest_urls):
            print("Downloading:", url)
            self.assertTrue(os.path.exists(dest))
            print("-> Passed:", dest)

    @unittest.skip('File is too big so it should be tested and monitored manually')
    def test_download_large_file(self):
        urls = [
            'ftp://speedtest.tele2.net/1GB.zip',
            'ftp://anonymous:anonymous@speedtest.tele2.net/10GB.zip'
        ]
        dest_urls = [self.downloader.download(url, self._build_dest_path(url)) for url in urls]
        for url, dest in zip(urls, dest_urls):
            print("Downloading:", url)
            self.assertTrue(os.path.exists(dest))
            print("-> Passed:", dest)


if __name__ == '__main__':
    unittest.main()
