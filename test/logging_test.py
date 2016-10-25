from os import path, makedirs
from testfixtures import LogCapture

import pytest

import prosper.common.prosper_logging as prosper_logging
from prosper.common.prosper_config import get_config
HERE = path.abspath(path.dirname(__file__))
LOCAL_CONFIG = path.join(HERE, 'common_config.cfg') #use /test config
if not path.isfile(LOCAL_CONFIG):   #else use /prosper/common config
    DEFAULT_PATH = path.join(path.dirname(HERE), 'prosper', 'common')
    LOCAL_CONFIG = path.join(DEFAULT_PATH, 'common_config.cfg')
TEST_CONFIG = get_config(LOCAL_CONFIG)

def test_logger(config_override=TEST_CONFIG):
    '''excercise logger utility'''
    logger = prosper_logging.create_logger(
        'test_logging',
        '.',
        config_override,
        'DEBUG'
    )
    with LogCapture('test_logging') as l:
        logger.debug('prosper.common.prosper_logging TEST --DEBUG--')
        logger.info('prosper.common.prosper_logging TEST --INFO--')
        logger.warning('prosper.common.prosper_logging TEST --WARNING--')
        logger.error('prosper.common.prosper_logging TEST --ERROR--')
        logger.critical('prosper.common.prosper_logging TEST --CRITICAL--')

    l.check(
        ('test_logging', 'DEBUG',    'prosper.common.prosper_logging TEST --DEBUG--'),
        ('test_logging', 'INFO',     'prosper.common.prosper_logging TEST --INFO--'),
        ('test_logging', 'WARNING',  'prosper.common.prosper_logging TEST --WARNING--'),
        ('test_logging', 'ERROR',    'prosper.common.prosper_logging TEST --ERROR--'),
        ('test_logging', 'CRITICAL', 'prosper.common.prosper_logging TEST --CRITICAL--'),
    )

if __name__ == '__main__':
    pass