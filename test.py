import sqlite3
import datetime
from datetime import date

def month():
    con = sqlite3.connect("db/db.db")
    cur = con.cursor()
    dt_now = date.today()
    month = str(dt_now)[:7]
    res = cur.execute("""SELECT sum(amount) 
                         FROM expense
                         JOIN category ON expense.category_codename=category.codename
                         where category.is_base_expense like ? and created like ?""",
                         (0, '%'+str(month)+'%',))
    base_result = res.fetchone()
    return (base_result[0])

print(month())