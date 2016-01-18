import time
import logging
import logging.config
from conf.config import LOGGING

logger = logging.getLogger(__name__)


def call_ok(ctx):
    time_used = (time.time() - ctx.st_time)*1000
    fmt = (' => {%s ms}' % str(time_used))
    logger.info(fmt)


def call_exc(ctx):
    time_used = (time.time() - ctx.st_time)
    fmt = (' => {time_used} => {ctx.exc}')
    logger.error(fmt, exc_info=True)


def call_warn(ctx):
    time_used = (time.time() - ctx.st_time)
    fmt = (' => {time_used}')
    logger.warn(fmt)


def logger_init():
    logging.config.dictConfig(LOGGING)
