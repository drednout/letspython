import MySQLdb

con = MySQLdb.connect('localhost', 'root', 'root', 'lesson12');

sql_data = {
    "id": 1,
    "code": "USD",
    "amount": 100,
}
sql_query = """UPDATE money SET amount=amount+%(amount)s WHERE player_id=%(id)s AND 
               code=%(code)s"""

with con:
    cur = con.cursor()
    cur.execute(sql_query, sql_data)
