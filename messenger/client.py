import socket, time, json

def presence(name):
    t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
    presence = {"action": "presence", "time": t, "type": "status",
                "user": {"account_name": name, "status": "Yep, I am here!"}}

    s.sendto(json.dumps(presence).encode(), server)
def auth(name, passwd,server):
    t = time.time()
    s.sendto(json.dumps({"action": "authenticate", "time": t, "user": {"account_name": name, "password": passwd}}).encode(),server)

host = 'localhost'
port = 9090
server = (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server)
name = 'Andrey'
passwd = 'MyPass'
auth(name,passwd, server)
while True:

    request = s.recv(1024)
    print(request.decode())
    presence(name)
s.close()