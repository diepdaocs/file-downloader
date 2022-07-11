import unittest

from file_downloader.config.config import Config


class ConfigTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config()

    def test_something(self):
        downloader = self.config.get('downloader')
        chunk_size = downloader.get('chunk_size')
        self.assertEqual(chunk_size, 8192)


if __name__ == '__main__':
    unittest.main()
