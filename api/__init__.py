from tornado.web import RequestHandler
import time
from core.signal import api_call_ok_sig

class BaseRequestHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseRequestHandler, self).__init__(application, request, **kwargs)
        self.ctx = ApiCtx(time.time())


class ApiCtx():
    def __init__(self, st_time):
        self.st_time = st_time
