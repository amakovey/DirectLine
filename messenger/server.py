import socket, time, json, select
import log_config

def logger(what):
    def wrap(w,data):
        what(w,data)
        log = log_config.logging.getLogger("app")
        for i in w:
            log.critical("Data %s sended to %s", data, i)
    return wrap

def read_msg(r):
    for i in r:
        data = i.recv(1024).decode('ascii')
        print (data)
    return data

@logger
def send_msg(w,data):
    for i in w:
        resp = data.encode('ascii')
        test_len = i.send(resp)

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
        data = read_msg(r)
    if w and data:
        send_msg(w,data)