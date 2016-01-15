from blinker import signal
from core.log import *
from pprint import pprint

api_call_sig = signal(1000)
api_call_exc_sig = signal(1001)
api_call_ok_sig = signal(1002)


def reg_signal():
    api_call_ok_sig.connect(call_ok)
    api_call_exc_sig.connect(call_exc)
    pprint('reg_signal_ok')
