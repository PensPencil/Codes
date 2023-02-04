import sqlite3
conn = sqlite3.connect("sql.db")

conn.execute("INSERT into movies VALUES(1,'Interstellar',9.0),(2,'Spiderman',7)")
conn.commit()
for i in conn.execute("Select * from movies"):
    print(i)