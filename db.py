import sqlite3
import datetime
from datetime import date


def con_cursor():
    con = sqlite3.connect("db.db")
    cur = con.cursor()


def add_expense(amount, created, category_codename, raw_text):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    sql_insert = """insert into expense(amount,created,category_codename,raw_text) 
                 values(?, ?, ?, ?);"""
    data = (amount, created, category_codename, raw_text)
    res = cur.execute(sql_insert, data)
    con.commit()


def month():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    dt_now = date.today()
    month = str(dt_now)[:7]
    res = cur.execute("SELECT SUM(amount) from expense where created like ?", ('%'+str(month)+'%',))
    base_result = res.fetchone()
    return (base_result[0])


# def month_category():
#     con = sqlite3.connect("db.db")
#     cur = con.cursor()
#     dt_now = date.today()
#     month = str(dt_now)[:7]
#     res = cur.execute(
#         "SELECT category_codename, sum(amount) as sum FROM expense where created like ? GROUP BY category_codename ",
#         ('%'+str(month)+'%',))
#     base_result = res.fetchmany()
#     return (base_result[0])
def month_category():
    cash = []
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    dt_now = date.today()
    month = str(dt_now)[:7]
    res = cur.execute(
            "SELECT category_codename, sum(amount) as sum FROM expense where created like ? GROUP BY category_codename ",
            ('%'+str(month)+'%',))
    base_result = res.fetchall()
    for i in base_result:
        cash.append(str(i[0]) + ":" + str(i[1]))
    return (cash)
# def get_today():
#     con = sqlite3.connect("db.db")
#     cur = con.cursor()
#     dt_now = date.today()
#     res = cur.execute("SELECT SUM(amount) from expense where created like ?", ('%'+str(dt_now)+'%',))
#     base_result = res.fetchone()
#     return (base_result[0])
def today_category():
    cash = []
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    dt_now = date.today()
    res = cur.execute(
            "SELECT category_codename, sum(amount) as sum FROM expense where created like ? GROUP BY category_codename ",
            ('%'+str(dt_now)+'%',))
    base_result = res.fetchall()
    for i in base_result:
        cash.append(str(i[0]) + ":" + str(i[1]))
    return (cash)

def delete_expense():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("DELETE from expense where id = (SELECT max(id) FROM expense)")
    con.commit()
