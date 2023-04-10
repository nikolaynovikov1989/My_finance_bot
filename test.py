import sqlite3
import datetime
from datetime import date

con = sqlite3.connect("db.db")
cur = con.cursor()
dt_now = date.today()
month = str(dt_now)[:7]
res = cur.execute(
    "SELECT category_codename, sum(amount) as sum FROM expense where created like ? GROUP BY category_codename ",
    ('%' + str(month) + '%',))
base_result = res.fetchall()
print(base_result)
