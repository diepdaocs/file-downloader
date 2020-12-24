import ftplib
import os
import shutil
from contextlib import closing
from urllib import request

from agoda.downloader import DownloaderIF, URL


class FTPDownloader(DownloaderIF):
    def download(self, url, dest_path):
        file_name = self.build_filename(url)
        file_path = os.path.join(dest_path, file_name)
        obj: URL = self.parse_url(url)
        if obj.username:
            with closing(ftplib.FTP()) as ftp:
                ftp.connect(obj.host, obj.port or 22)
                ftp.login(obj.username, obj.password)
                ftp.cwd(obj.path)
                with open(file_path, 'wb') as local_file:
                    ftp.retrbinary("RETR " + file_name, local_file.write)
        else:
            with closing(request.urlopen(obj.url)) as r:
                with open(file_path, 'wb') as f:
                    shutil.copyfileobj(r, f)

        return file_path
