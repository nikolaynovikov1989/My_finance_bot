import sqlite3
text = "100 авто"
vars = text.split(" ")
aliases_name = vars[1]


con = sqlite3.connect("db.db")
cur = con.cursor()
res = cur.execute("SELECT codename from category where aliases like ?",('%' + aliases_name + '%',))
base_result = res.fetchone()
print(base_result)

# for x in base_result:
#     if vars[1] in x:
#         print("Есть")

# for x in base_result:
#     for n in x:
#      if vars[1] in n:
#         print("GOoooooOOOooooOOOOOOOOODDDD")