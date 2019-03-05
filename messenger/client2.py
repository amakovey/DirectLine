import socket, time, json, sys
import JIM
import dbclient
import threading

host = 'localhost'
port = 9090
server = (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server)
name = "Edward"
pasw = "pass"
user = JIM.Client(name,pasw)
userdb = dbclient.DbStore(name)
userdb.create_db()
user.auth(s)

def client_receive(user, s):
    while True:

        data = s.recv(1024).decode('ascii')
        a = json.loads(data)
        global cl_clist
        try:
            cl_clist = []
            if a["response"] == 202:
                cl_clist = user.allcontacts(s, a)
                print (cl_clist)
        except:
            pass
        if a["action"] =="msg":
            print (a["message"])
    s.close()
def client_write():
     list = []
     while True:
        msg = input()
        if msg == "get": #Команда для запроса списка клиентов с сервера
            user.getcontacts(s)
        elif msg[0:4] == "add ":#Команда для добавления клиента в контакты клиента
            client_id = msg[4:len(msg)]
            if client_id in cl_clist:
                userdb.add_client(client_id)
            else:
                print("Wrong user")
        elif msg[0:4] == "del ":#Команда для удаления клиента из контактов клиента
            client_id = msg[4:len(msg)]
            if client_id in cl_clist:
                userdb.del_client(client_id)
            else:
                print("Wrong user")
        elif msg[0:5] == "join " and len(msg)>5:
            a = user.join(s, msg[5:len(msg)])
            print (a)
        elif msg == "exit":
            break
        else:
            user.msg(s, name, "Petya", msg)
rT = threading.Thread(target=client_receive, args=(user, s))

rT.start()





client_write()
s.close()