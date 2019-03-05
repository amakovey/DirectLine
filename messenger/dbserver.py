import sqlite3


class DbStore():
    def create_db():
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS client(client_id TEXT PRIMARY KEY,'
                    'info TEXT)')
        cur.execute('CREATE TABLE IF NOT EXISTS history_login(time TEXT,'
                    'ip TEXT)')
        cur.execute('CREATE TABLE IF NOT EXISTS contacts(owner_id INTEGER,'
                    'client_id TEXT)')

        cur.execute('CREATE TABLE IF NOT EXISTS history_client(client_id INTEGER,'
                    'time TEXT,'
                    'message TEXT)')
        cur.close()
        con.close()

    def login(ip, t):
        data = [str(t), str(ip)]
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        cur.execute('INSERT INTO history_login VALUES (?,?)', data)
        con.commit()
        cur.close()
        con.close()

    def client(user):
        data = [user, "Some info about client"]
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        try:
            cur.execute('INSERT INTO client VALUES (?,?)', data)
            con.commit()
        except:
            pass
        cur.close()
        con.close()

    def get_login():
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        client = []
        try:
            cur.execute('SELECT client_id FROM client')
            result = cur.fetchall()
            for i in result:
                client.append(i[0])
            con.commit()
        except:
            pass

        cur.close()
        con.close()
        return client
