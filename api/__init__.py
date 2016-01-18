from tornado.web import RequestHandler
import time
import functools
from core.signal import api_call_ok_sig, api_call_exc_sig


class BaseRequestHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseRequestHandler, self).__init__(application, request, **kwargs)


class ApiCtx():
    def __init__(self):
        self.st_time = None
        self.exc = None


def Api(rule):
    def _wrapper(func):
        ctx = ApiCtx()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                ctx.st_time = time.time()
                func(*args, **kwargs)
                api_call_ok_sig.send(ctx)
            except Exception as e:
                ctx.exc = e
                api_call_exc_sig.send(ctx)
                raise e

        return wrapper

    return _wrapper
