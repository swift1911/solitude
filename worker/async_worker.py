from celery import Celery
import logging
import gevent
from conf.config import REDIS, ASYNC_CONFIG


def init_redis_config():
    redis_host = REDIS.get('host')
    redis_port = REDIS.get('port')
    redis_passwd = REDIS.get('password')
    return 'redis://:%s@%s:%s/1' % (redis_passwd, redis_host, redis_port)


def init_rabbit_mq_config():
    return ''


def init_celery_app_config():
    return init_rabbit_mq_config() if ASYNC_CONFIG.get('mode') == 'rabbitmq' else init_redis_config()


default_config = init_celery_app_config()

celeryapp = Celery('solitude_async', backend=default_config, broker=default_config)
logger = logging.getLogger(__name__)


@celeryapp.task
def async_send_task(func, retry=3, *args, **kwargs):
    while retry:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            retry -= 1
            gevent.sleep(1)
