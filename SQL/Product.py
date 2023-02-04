import sqlite3

conn=sqlite3.connect('product.db')

conn.execute('''CREATE TABLE IF NOT EXISTS Orderitem(
    ID VARCHAR(20),
    Order_ID VARCHAR(20) NOT NULL,
    Product_ID VARCHAR(20) NOT NULL,
    Unit_price INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    FOREIGN KEY (Order_ID) REFERENCES Product(Order_ID)
);


''')

conn.execute('''CREATE TABLE IF NOT EXISTS Product(
    ID VARCHAR(20),
    Product_name TEXT NOT NULL,
    supplier_ID VARCHAR(20) NOT NULL,
    Unit_Price INTEGER NOT NULL,
    Package INTEGER NOT NULL,
    Order_ID VARCHAR(20) PRIMARY KEY NOT NULL
);
''')
conn.execute('''INSERT INTO Product(ID, Product_name, Supplier_ID, Unit_price, Package, Order_ID)
            VALUES  ('A17GHVF72C', 'Bingo! Original Style Salt Sprinkled', 'VH7793VN6G', 40, 10, 'HG6378FG8B'),
                    ('CG673NMFBJ','Slurrp Farm Little Millet Noodles','BVJH674FG6', 300, 2, 'GHGHF67486'),
                    ('G6R78BFNNV', 'Britannia Little Hearts', 'GH56HNK78K', 22, 40, 'GH562JK235'),
                    ('HG674695T9', 'Cadbury Oreo Dipped Cookie', 'KJ76R3BFFB', 56, 12, 'HGHJ56487F'),
                    ('JGF6723VNL', 'Nutella Hazelnut Spread with Cocoa', 'H64783VKV', 342, 5, 'JHD678236B')
            
''')

conn.execute('''INSERT INTO Orderitem(ID, Order_ID, Product_ID, Unit_price, Quantity)
            VALUES  ('A17GHVF72C', 'HG6378FG8B', 'GH6754679H', 600, 20),
                    ('CG673NMFBJ', 'GHGHF67486', 'JKVDB378FG', 165, 7),
                    ('G6R78BFNNV', 'GH562JK235', 'NKJD6875VV', 424, 8),
                    ('HG674695T9', 'HGHJ56487F', 'NVJKH63783', 136, 10),
                    ('JGF6723VNL', 'JHD678236B', 'NLUW576VDF', 250, 15)
            
''')

print('Product_ID    Product_name    Quantity')
query = "SELECT Product_ID, Product_name, Quantity FROM Orderitem, Product WHERE Product.Order_ID=Orderitem.Order_ID ORDER BY 1,2,3;"

for i in conn.execute(query):
    print(i)
    
print('\n\n')
print('Product_name                  Order_ID                 Supplier_ID')
query = "SELECT Product_name, Product.Order_ID, Supplier_ID FROM Orderitem, Product WHERE Product.Order_ID=Orderitem.Order_ID ORDER BY 1,2,3;"

for i in conn.execute(query):
    print(i)
