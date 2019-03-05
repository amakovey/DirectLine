import sqlite3


class DbStore():
    def __init__(self, name):
        self.name = name

    def create_db(self):
        print(self.name)
        con = sqlite3.connect(str(self.name) + '.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS history_message(client_id INTEGER,'
                    'time TEXT,'
                    'message TEXT)')
        cur.execute('CREATE TABLE IF NOT EXISTS contacts(client_id TEXT PRIMARY KEY)')

        cur.close()
        con.close()

    def add_client(self, client_id):
        con = sqlite3.connect(self.name + '.db')
        cur = con.cursor()
        data = [client_id]
        try:
            cur.execute('INSERT INTO contacts VALUES (?)', data)
            con.commit()
            print("Success")
        except:
            print('User %s already in your contacts' % client_id)
        cur.close()
        con.close()

    def del_client(self, client_id):

        con = sqlite3.connect(self.name + '.db')
        cur = con.cursor()
        try:
            cur.execute('DELETE FROM contacts WHERE client_id ="' + str(client_id) + '"') # Как вызвать ошибку при
            # попытке удаления несуществующей записи?
            con.commit()
            print ("Success")
        except:
            print('User %s not found' % client_id)
        cur.close()
        con.close()
