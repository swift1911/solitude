from api.push import PingApi, PushApi
from core.signal import reg_signal

api_container = [
    (r"/ping", PingApi),
    (r"/push", PushApi)

]

reg_signal()
