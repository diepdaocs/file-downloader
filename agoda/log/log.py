import os
import logging.config
import yaml

import logging


def setup_logging(config_file=None):
    if not config_file:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.join(dir_path, 'config.yaml')
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
