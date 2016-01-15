from api import BaseRequestHandler, Api
from service.push import ApnsProvider
from core.signal import api_call_ok_sig
from core.log import call_ok


class PingApi(BaseRequestHandler):
    @Api('ping')
    def get(self):
        self.write('pong')


class PushApi(BaseRequestHandler):
    @Api('push')
    def get(self):
        return 'METHOD NOT ALLOWED'

    @Api('push')
    def post(self, *args, **kwargs):
        provider = ApnsProvider()
        provider.send()
