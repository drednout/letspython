import MySQLdb

con = MySQLdb.connect('localhost', 'root', '1', 'lesson12');

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM players")
    for row in cur.fetchall():
        print(row)
