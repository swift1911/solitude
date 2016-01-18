from api import BaseRequestHandler, Api
from service.push import ApnsProvider


class PingApi(BaseRequestHandler):
    @Api('ping')
    def get(self):
        self.write('pong')


class PushApi(BaseRequestHandler):
    @Api('push')
    def post(self, *args, **kwargs):
        provider = ApnsProvider()
        provider.send(1, 'asf', 'content', {
            'category': 'test'
        })
