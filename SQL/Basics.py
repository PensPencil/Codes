import sqlite3
conn = sqlite3.connect('Basics.db')
print("Database created successfully !!!")
conn.execute("""CREATE TABLE IF NOT EXISTS SCHOOL 
(ID PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL );""")
conn.execute("""INSERT INTO SCHOOL(ID,NAME,AGE)
VALUES(1,"Sidd",19),
(2,"Sarthak",19),
(3,"Samridh",20);""")
print("Database updated successfully !!!")

query='UPDATE SCHOOL SET NAME = "FOODIE" WHERE ID = 3;'
conn.execute(query)    
query='SELECT * FROM SCHOOL;'
for i in conn.execute(query):
    print(i)
print(conn.total_changes)