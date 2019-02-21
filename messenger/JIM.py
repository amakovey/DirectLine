import json
import time
from log_config import log
class Response:
    @log
    def send(r):
        for i in r:
            data = i.recv(1024).decode('ascii')
            t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
            responce = json.dumps({"action": 100, "time": t, "alert": "OK"})
            resp = responce.encode('ascii')
            test_len = i.send(resp)
        return data

class Message:
    @log
    def send(w, data):
        for i in w:

            t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

            message = json.dumps({"action": "msg", "time": t, "to": "who", "from": "me", "encoding": "ascii", "message": data })
            resp = message.encode('ascii')
            test_len = i.send(resp)
