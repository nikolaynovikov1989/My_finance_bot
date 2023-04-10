import sqlite3
from datetime import date

con = sqlite3.connect("db.db")
cur = con.cursor()
cur.execute("DELETE from expense where id = (SELECT max(id) FROM expense)")
con.commit()