import socket, time, json, select
from log_config import log
import JIM

host = 'localhost'
port = 9090
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
s.settimeout(0.2)
clients=[]
while True:
    data=''
    try:
        conn, addr = s.accept()
    except OSError as e:
        pass
    else:
        print("Получен запрос на соединение с %s" % str(addr))
        clients.append(conn)
    finally:
        wait = 0
        r = []
        w = []
        try:
            r, w, e = select.select(clients, clients, [], wait)
        except:
            pass

    if r:
        data = JIM.Response.send(r)
    if w and data:
        JIM.Message.send(w, data)