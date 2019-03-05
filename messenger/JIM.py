import json
import time
import dbserver
from log_config import log


class Response:
    # @log
    def receive(r):
        a = {}
        for i in r:
            try:
                data = i.recv(1024).decode('ascii')
                if data:
                    a[i] = json.loads(data)
            except:
                pass
        return a

    def send(w, data, clients):

        for key, value in data.items():

            if value["action"] == "get_contacts":
                ContactList.sendcontacts(key, value)
            if value["action"] == "authenticate":
                Response.auth(key, value)
            if value["action"] == "join":
                Response.join(key, value)
            if value["action"] == "msg":
                Response.msg(key, value, clients)

    def auth(r, data):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        dbserver.DbStore.login(r, t)
        user = data["user"]
        dbserver.DbStore.client(user["account_name"])

    def join(r, data):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print ("R", r)
        print ("DATA", data)
    def msg(r, data, clients):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        for i in clients:
            message = json.dumps(data)
            resp = message.encode('ascii')
            test_len = i.send(resp)



class ContactList:
    def addcontact(s, nickname):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        message = json.dumps({"action": "add_contact", "user_id": nickname, "time": t})
        resp = message.encode('ascii')
        test_len = s.send(resp)
        data = s.recv(1024).decode('ascii')
        return (json.loads(data))

    def delcontact(s, nickname):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        message = json.dumps({"action": "del_contact", "user_id": nickname, "time": t})
        resp = message.encode('ascii')
        test_len = s.send(resp)
        data = s.recv(1024).decode('ascii')
        return (json.loads(data))

    def sendcontacts(r, data):
        client_list = dbserver.DbStore.get_login()
        quantity_clients = len(client_list)
        message = json.dumps({"response": 202, "quantity": quantity_clients})
        resp = message.encode('ascii')
        test_len = r.send(resp)
        for j in range(quantity_clients):
            time.sleep(0.01)
            message = json.dumps({"action": "contact_list", "user_id": client_list[j]})
            resp = message.encode('ascii')
            test_len = r.send(resp)


class Client:
    def __init__(self, name, pasw):
        self.name = name
        self.pasw = pasw

    def leave(s):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        message = json.dumps({"action": "leave", "time": t, "room": "room_name"})
        resp = message.encode('ascii')
        s.send(resp)

    def join(self, s, room):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        message = json.dumps({"action": "join", "time": t, "room": room})
        resp = message.encode('ascii')
        s.send(resp)
        data = s.recv(1024).decode('ascii')
        a = json.loads(data)
        return a

    def auth(self, s):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        message = json.dumps(
            {"action": "authenticate", "time": t, "user": {"account_name": self.name, "password": self.pasw}})
        resp = message.encode('ascii')
        s.send(resp)

    def presence(s, name):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        message = json.dumps({"action": "presence", "time": t, "type": "status",
                              "user": {"account_name": name, "status": "Yep, I am here!"}})
        resp = message.encode('ascii')
        s.send(resp)

    def getcontacts(self, s):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        message = json.dumps({"action": "get_contacts", "time": t})
        resp = message.encode('ascii')
        s.send(resp)

    def allcontacts(self, s, a):
        q = a["quantity"]
        cl_clist=[]
        for i in range(q):
            try:
                data = s.recv(1024).decode('ascii')
                n = json.loads(data)
                cl_clist.append(n["user_id"])
            except:
                pass
        return cl_clist
    def msg(self, s, who, me, data):
        t = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        message = json.dumps({"action": "msg", "time": t, "to": "who", "from": "me", "encoding": "ascii", "message": data })
        resp = message.encode('ascii')
        test_len = s.send(resp)