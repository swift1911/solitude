import tornado.ioloop
import tornado.web
from service import api_container
from pprint import pprint

app = tornado.web.Application(api_container)

if __name__ == "__main__":
    app.listen(9294, '0.0.0.0')
    pprint('start listening %s:%s....' % ('0.0.0.0', '9294'))
    tornado.ioloop.IOLoop.instance().start()
