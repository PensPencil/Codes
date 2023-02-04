import sqlite3

conn = sqlite3.connect('recipes.db')

conn.execute('''CREATE TABLE IF NOT EXISTS recipes(
    id INTEGER PRIMARY KEY,
    name VARCHAR(400) NOT NULL,
    description TEXT NOT NULL,
    category_id INT(11) NOT NULL,
    chef_id INT(255) NOT NULL,
    created datetime
);
''')
conn.execute('''INSERT INTO recipes (id,name,description,category_id,chef_id,created) 
                VALUES(1,'Dosa','Indian',1,'BL000002','2022-4-4'),
                    (2,'Noodles','Chinese',2,'BL000002','2022-4-3'),
                    (3,'Pizza','Italy',14,'BL000004','2022-4-7'),
                    (4,'Pongal','Indian',15,'BL000003','2022-4-5')''')
count=0
query = "SELECT * FROM recipes WHERE description = 'Chinese';"
for i in conn.execute(query):
    count=count+1
print("Total number of Chinese recepies :",count,"\n")


print("Recipes with chef_id 'BL000002':")
query = "SELECT id, name FROM recipes WHERE chef_id='BL000002'"
for i in conn.execute(query):
    print(i)
    
print("\nDescription of the recipes whose name begins with 'P':")
query = "SELECT description FROM recipes WHERE name LIKE 'P%'"
for i in conn.execute(query):
    print(i)
