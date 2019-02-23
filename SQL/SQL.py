import sqlite3


def create_db():
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS competition(competition_id INTEGER PRIMARY KEY,'
                'competition_name TEXT,'
                'world_record TEXT,'
                'set_date TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS result(competition_id INTEGER,'
                'sportsman_id INTEGER,'
                'result TEXT,'
                'city TEXT,'
                'hold_date TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS sportsman(sportsman_id INTEGER PRIMARY KEY,'
                'sportsman_name TEXT,'
                'rank INTEGER,'
                'year_of_birth TEXT,'
                'personal_record INTEGER,'
                'country TEXT)')
    cur.close()
    con.close()


def add_db2(data, name):
    n = (len(data[0])) - 1
    q = ',?'
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    query = 'INSERT INTO ' + name + ' VALUES (?' + q * n + ')'
    for i in data:
        cur.execute(query, i)
        con.commit()


def make_table():
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    cur2 = con.cursor()
    cur2.execute('CREATE TABLE IF NOT EXISTS new_table(competition_id INTEGER,'
                 'competition_name TEXT,'
                 'world_record TEXT,'
                 'set_date TEXT)')
    cur.execute('SELECT * FROM competition WHERE competition_id = 1')
    for row in cur:
        cur2.execute('INSERT INTO new_table VALUES (?,?,?,?)', row)
        con.commit()
    cur.close()
    cur2.close()
    con.close()

def print_table(query):
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    cur.execute(query)
    for row in cur:
        print(row)
    cur.close()
    con.close()
    print('----------')


competition = [[1, "Biathlon", "12", "01/01/1999"],
               [2, "Running", "15", "01/05/1995"],
               [3, "Swimming", "30", "01/02/1993"]]


result = [[1, 1, 10, "Togliatti", "12-05-2010"],
          [1, 2, 0, "Togliatti", "12-05-2010"],
          [1, 3, 12, "Togliatti", "12-05-2010"],
          [1, 4, 9, "Togliatti", "12-05-2010"],
          [1, 5, 8, "Togliatti", "12-05-2010"],
          [2, 6, 15, "Samara", "15-05-2010"],
          [2, 7, 2, "Samara", "15-05-2010"],
          [2, 8, 3, "Samara", "15-05-2010"],
          [2, 9, 4, "Samara", "15-05-2010"],
          [2, 10, 0, "Samara", "15-05-2010"],
          [3, 11, 10, "Moscow", "01-02-1993"],
          [3, 12, 30, "Moscow", "01-02-1993"],
          [3, 13, 13, "Moscow", "01-02-1993"],
          [3, 14, 15, "Moscow", "01-02-1993"],
          [3, 15, 17, "Moscow", "01-02-1993"],
          [3, 16, 19, "Moscow", "01-02-1993"],
          [3, 17, 9, "Moscow", "01-02-1993"]]


sportsman = [[1, "Ivanov A.A.", 1, "1970", 10, "Russia"],
             [2, "Petrov I.I.", 2, "1969", 8, "Slovenia"],
             [3, "Sidorov P.T.", 3, "1990", 12, "Italia"],
             [4, "Frolov C.T.", 2, "1990", 13, "Germany"],
             [5, "Vern J.F.", 1, "1991", 9, "France"],
             [6, "Smith A.E.", 3, "1992", 15, "USA"],
             [7, "Rotaru I.G.", 1, "1981", 9, "Moldova"],
             [8, "Petrenko A.S.", 1, "1985", 19, "Ukraine"],
             [9, "Damm J.C.", 3, "1986", 4, "Belgium"],
             [10, "Bulba T.A.", 2, "1987", 7, "Belarus"],
             [11, "Erkn A.V.", 1, "1988", 3, "Kazakhstan"],
             [12, "Felisto D.J.", 2, "1971", 30, "Spain"],
             [13, "Drozdov D.E.", 1, "1982", 31, "Russia"],
             [14, "Markov I.O.", 1, "1983", 32, "Ukraine"],
             [15, "Potapenko O.I.", 1, "1984", 29, "Belarus"],
             [16, "Dubok L.H.", 1, "1985", 28, "Moldova"],
             [17, "Trump D.J.", 1, "1986", 35, "USA"]]


# 1. Создать таблицы competition, result, sportsman
create_db()

# 2. Заполните таблицы тестовыми данными с помощью команды INSERT
add_db2(competition, "competition") # При повторном запуске будет ругаться, т.к. в таблице Primary key
add_db2(result, "result")
add_db2(sportsman, "sportsman")# При повторном запуске будет ругаться, т.к. в таблице Primary key

# 3. Создать таблицу как результат выполнения команды SELECT
make_table()

# 4. Выдайте всю информацию о спортсменах из таблицы sportsman.
print_table('SELECT * FROM sportsman')

# 5. Выдайте наименование и мировые результаты по всем соревнованиям.
print_table('select competition.competition_name, result.result FROM competition, result WHERE competition.competition_id = result.competition_id')

# 6. Выберите имена всех спортсменов, которые родились в 1990 году.
print_table('select * from sportsman where year_of_birth = "1990"')

# 7. Выберите наименование и мировые результаты по всем соревнованиям, установленные
# 12-05-2010 или 15-05-2010.
print_table('select competition.competition_name, result.result FROM competition, result WHERE competition.competition_id = result.competition_id and (result.hold_date = "15-05-2010" or result.hold_date = "12-05-2010")')

# 8. Выберите дату проведения всех соревнований, проводившихся в Москве и полученные на
# них результаты равны 10 секунд.
print_table('select hold_date FROM result WHERE city ="Moscow" and result = 10')

# 9. Выберите имена всех спортсменов, у которых персональный рекорд менее 25 с.
print_table('select sportsman_name FROM sportsman WHERE personal_record < 25')