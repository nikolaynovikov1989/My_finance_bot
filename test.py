import sqlite3
from datetime import date

def get_today():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    dt_now = date.today()
    res = cur.execute("SELECT SUM(amount) from expense where created like ?", ('%'+str(dt_now)+'%',))
    base_result = res.fetchone()
    print(base_result[0])

get_today()