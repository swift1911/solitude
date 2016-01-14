from blinker import signal

api_call_sig = signal(1000)
api_call_exc_sig = signal(1001)
api_call_ok_sig = signal(1002)
