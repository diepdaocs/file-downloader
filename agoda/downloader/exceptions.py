class DownloadException(Exception):
    def __init__(self, url):
        self.message = 'Error while downloading url: ' + str(url)
        super().__init__(self.message)
