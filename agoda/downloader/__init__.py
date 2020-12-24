from abc import ABCMeta, abstractmethod
from urllib.parse import urlparse, ParseResult


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
    @staticmethod
    def parse_url(url) -> URL:
        obj: ParseResult = urlparse(url)
        return URL(url, obj.scheme, obj.username or '', obj.password or '', obj.hostname, obj.port, obj.path)

    @abstractmethod
    def download(self, url, dest_path) -> str:
        """
        Download file and return the stored location
        """
        pass
