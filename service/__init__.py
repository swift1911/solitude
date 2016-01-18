from api.push import PingApi, PushApi
from core.signal import reg_signal
from core.log import logger_init

api_container = [
    (r"/ping", PingApi),
    (r"/push", PushApi)

]

reg_signal()

logger_init()
