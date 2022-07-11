import logging
import unittest
from unittest.mock import Mock

from file_downloader.downloader.download import Download
from file_downloader.downloader.exceptions import UnsupportedProtocolException, DownloadException
from file_downloader.log.log import setup_logging


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        setup_logging()
        self.dest_path = 'tests/data'
        self.downloader_factory = Mock()
        self.downloader = Mock()
        self.download = Download(self.dest_path, self.downloader_factory)

    def test_error(self):
        urls = ['https://www.facebook.com/favicon.ico',
                'https://www.google.com/favicon.ico',
                # 'ftp://speedtest.tele2.net/512KB.zip',
                # 'ftp://anonymous:anonymous@speedtest.tele2.net/1MB.zip'
                ]
        self.downloader_factory.get.return_value = self.downloader
        self.downloader.download_url.side_effect = DownloadException(urls[0])

        logger = logging.getLogger('Download')
        with self.assertLogs(logger=logger, level='INFO') as cm:
            self.download.download_urls(urls)
            # self.assertTrue(cm.output[2].startswith('ERROR:Download:Error while downloading url'))

        # with self.assertRaises(DownloadException):
        #     self.downloader.download_url(urls[0])

        self.download.download_urls(urls)

        # self.downloader.download_url.assert_called()


if __name__ == '__main__':
    unittest.main()
