import socket, time, json, sys

host = 'localhost'
port = 9090
server = (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server)

def client_read():
    while True:
        data = s.recv(1024).decode('ascii')
        a = json.loads(data)
        print('Ответ:', a["message"])

    s.close()

def client_write():
    while True:
        msg = input('Ваше сообщение: ')
        if msg == 'exit':
            break
        s.send(msg.encode('ascii'))  # Отправить!
    s.close()


if len(sys.argv) <2:
    print ("Недостаточно параметров (w - write/r - read)")
elif sys.argv[1] == 'r':
    client_read()
elif sys.argv[1] == 'w':
    client_write()
else:
    print ("Неверный ключ (w - write/r - read)")
