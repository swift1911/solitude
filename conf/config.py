'''
    This is the config of solitude
'''

REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': ''
}

'''
    This is the config of async mode
    redis and rabbitmq can be choosed
'''
ASYNC_CONFIG = {
    'mode': 'redis'
}
