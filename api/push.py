from api import BaseRequestHandler
from service.push import ApnsProvider


class PingApi(BaseRequestHandler):
    def __init__(self):
        super(BaseRequestHandler, self).__init__('ping')

    def get(self):
        return 'ping ok'


class PushApi(BaseRequestHandler):
    def __init__(self):
        super(BaseRequestHandler, self).__init__('push')

    def get(self):
        return 'METHOD NOT ALLOWED'

    def post(self, *args, **kwargs):
        provider = ApnsProvider()
        provider.send()
