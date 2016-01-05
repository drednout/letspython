import MySQLdb

con = MySQLdb.connect('localhost', 'root', 'root', 'lesson12');

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM players")
    for row in cur.fetchall():
        print(row)
