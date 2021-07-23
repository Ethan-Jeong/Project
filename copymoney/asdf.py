import sqlite3

con = sqlite3.connect('./db.sqlite3')
print(type(con))

cursor = con.cursor()
cursor.execute("SELECT 고가 FROM sum_bitcoin_gpu;")
rows = cursor.fetchall()
print(rows)
# for row in rows:
#     print(row)

con.close()
