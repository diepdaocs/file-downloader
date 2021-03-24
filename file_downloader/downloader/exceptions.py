class DownloadException(Exception):
    def __init__(self, url):
        self.message = 'Error while downloading url: ' + str(url)
        super().__init__(self.message)


class UnsupportedProtocolException(Exception):
    def __init__(self, url):
        protocol = url.split(':')[0]
        self.message = 'Unsupported protocol: %s' % protocol
        super().__init__(self.message)


class MissingProtocolException(Exception):
    def __init__(self, url):
        self.message = 'Missing protocol in url: %s' % url
        super().__init__(self.message)
