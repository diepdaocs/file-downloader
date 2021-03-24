import os

import yaml

from file_downloader.common.singleton import Singleton


class Config(object, metaclass=Singleton):
    def __init__(self, config_file=None):
        if not config_file:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            config_file = os.path.join(dir_path, 'config.yaml')
        self._configs = self._load(config_file)

    @staticmethod
    def _load(config_file):
        with open(config_file, 'r') as f:
            configs = yaml.safe_load(f.read())

        return configs

    def get(self, name):
        return self._configs.get(name)
