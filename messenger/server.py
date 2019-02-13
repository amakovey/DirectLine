import socket, time, json

def probe(addr):
    t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
    client.sendto(json.dumps({"action": "probe", "time": t}).encode(),addr)
    request = client.recv(1024)
    print (json.loads(request.decode()))

host = 'localhost'
port = 9090
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
clients=[]
while True:
    client, addr = s.accept()
    request = client.recv(1024)
    if addr not in clients:
        clients.append(addr)
        print(addr, ' is Connected')
    probe(addr)