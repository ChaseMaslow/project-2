#
#   Configuration classes
#

import configparser
import os
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)

config_file_paths = ['default.ini', 'credentials.ini']

def configure():
    cfg = configparser.ConfigParser()
    
    cfg.read(config_file_paths)
    if cfg.has_option('DEFAULT', 'author'):
        log.info(" - Configuring from credentials.ini")
    else:
        log.info(" - Configuring from default.ini")
    
    return cfg