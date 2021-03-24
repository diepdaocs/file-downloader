import ftplib
from contextlib import closing

from file_downloader.config.config import Config
from file_downloader.downloader import DownloaderIF, URL


class FTPDownloader(DownloaderIF):
    def __init__(self):
        self.configs = Config()

    def download(self, url, dest_path):
        obj: URL = self.parse_url(url)
        with closing(ftplib.FTP()) as ftp:
            ftp.connect(obj.host, obj.port or 21)
            ftp.login(obj.username or 'anonymous', obj.password or 'anonymous')
            parts = [p for p in obj.path.split('/') if p]
            path = '/'.join(parts[:-1])
            if path:
                ftp.cwd(obj.path)
            server_file_name = parts[-1]
            with open(dest_path, 'wb') as dest_file:
                ftp.retrbinary("RETR " + server_file_name, dest_file.write,
                               blocksize=self.configs.get('downloader')['chunk_size'])

        return dest_path
