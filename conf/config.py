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

MYSQL = {
    'master': {
        'host': '127.0.0.1',
        'passwd': 'root',
        'user': 'root',
        'port': 3306,
        'database': 'test'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'handlers': ['console', 'exception', 'all'],
        'level': 'INFO'
    },
    'loggers': {
        'exception': {
            'handlers': ['exception'],
            'propagate': True,
            'level': 'ERROR'
        },
        'all': {
            'handlers': ['all'],
            'propagate': True,
            'level': 'INFO'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'all': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': '/var/log/solitude.log',
            'mode': 'a',
            'maxBytes': 262144000,
            'backupCount': 10,
        },
        'exception': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'filename': '/var/log/solitude_err.log',
            'mode': 'a',
            'maxBytes': 262144000,
            'backupCount': 10,
        },
    }
}
