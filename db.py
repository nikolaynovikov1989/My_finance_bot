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
def get_expense():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    res = cur.execute("SELECT SUM(amount) from expense")
    base_result = res.fetchone()
    return (base_result[0])
def month():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    dt_now = date.today()
    month = str(dt_now)[:7]
    res = cur.execute("SELECT SUM(amount) from expense where created like ?", ('%'+str(month)+'%',))
    base_result = res.fetchone()
    return (base_result[0])
def month_category():
    cash = []
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    dt_now = date.today()
    month = str(dt_now)[:7]
    res = cur.execute("SELECT amount, category_codename from expense where created like ?", ('%' + str(month) + '%',))
    base_result = res.fetchall()
    for i in base_result:
        cash.append(i)
    return (cash)

def get_today():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    dt_now = date.today()
    res = cur.execute("SELECT SUM(amount) from expense where created like ?", ('%'+str(dt_now)+'%',))
    base_result = res.fetchone()
    return (base_result[0])