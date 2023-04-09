import sqlite3
from datetime import date

cash = []
con = sqlite3.connect("db.db")
cur = con.cursor()
dt_now = date.today()
month = str(dt_now)[:7]
res = cur.execute("SELECT amount, category_codename from expense where created like ?", ('%' + str(month) + '%',))
base_result = res.fetchall()
for i in base_result:
    cash.append(i)

answer_message = cash
for i in answer_message:
    print(i)