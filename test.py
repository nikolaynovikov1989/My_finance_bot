import sqlite3
con = sqlite3.connect("db.db")
cur = con.cursor()
text = "100 газировка"
vars = text.split(" ")
aliases_name = vars[1]
try:
 res = cur.execute("SELECT codename from category where aliases like ?", ('%' + aliases_name + '%',))
 base_result = res.fetchone()
 codename = base_result[0]
 print(codename)
except:
    codename = "other"
    print(codename)



# add_expense(vars[0], datetime.datetime.now(), codename, message.text)