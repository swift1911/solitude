from api import BaseRequestHandler
from service.push import ApnsProvider
import json


class PingApi(BaseRequestHandler):
    def get(self):
        self.write('pong')


class PushApi(BaseRequestHandler):
    def post(self, *args, **kwargs):
        push_token = self.get_argument('push_token')
        push_id = 1
        push_type = 2 if self.get_argument('type') != 'content' else 1
        raw_content = self.get_argument('content')
        provider = ApnsProvider()
        provider.send(push_id, push_token, push_type, json.loads(raw_content))
