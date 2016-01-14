from api.push import PingApi, PushApi

api_container = [
    (r"/ping", PingApi),
    (r"/push", PingApi)

]
