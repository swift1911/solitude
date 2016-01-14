from tornado.web import RequestHandler


class BaseRequestHandler(RequestHandler):
    def __init__(self, route=None, ctx=None):
        self.route = route
        self.ctx = ctx
