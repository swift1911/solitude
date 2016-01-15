import time
import logging

logger = logging.getLogger(__name__)


def call_ok(ctx):
    time_used = (time.time() - ctx.st_time) * 1000
    fmt = (' => {time_used}')
    logger.info(fmt)


def call_exc(ctx):
    time_used = (time.time() - ctx.st_time) * 1000
    fmt = (' => {time_used}')
    logger.error(fmt, exc_info=True)


def call_warn(ctx):
    time_used = (time.time() - ctx.st_time) * 1000
    fmt = (' => {time_used}')
    logger.warn(fmt)
