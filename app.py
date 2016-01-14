import tornado.ioloop
import tornado.web
from service import api_container

app = tornado.web.Application(api_container)

if __name__ == "__main__":
    app.listen(9294)
    tornado.ioloop.IOLoop.instance().start()
