from api import BaseRequestHandler
from service.push import ApnsProvider


class PingApi(BaseRequestHandler):
    def get(self):
        return 'ping ok'


class PushApi(BaseRequestHandler):
    def get(self):
        return 'METHOD NOT ALLOWED'

    def post(self, *args, **kwargs):
        provider = ApnsProvider()
        provider.send()
