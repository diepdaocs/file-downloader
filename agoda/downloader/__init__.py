import re
from abc import ABCMeta, abstractmethod


class URL(object):
    def __init__(self, url, protocol, username, password, host, port, path):
        self.url = url
        self.protocol = protocol
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.path = path


class DownloaderIF(metaclass=ABCMeta):
    def parse_url(self, url) -> URL:
        pass

    @staticmethod
    def build_filename(url) -> str:
        return re.sub(r'[:/]', '-', url)

    @abstractmethod
    def authenticate(self, url: URL) -> bool:
        pass

    @abstractmethod
    def download(self, url, dest_path) -> str:
        """
        Download file and return the stored location
        """
        pass
