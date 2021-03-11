import sqlite3
con = sqlite3.connect('database.db')
c = con.cursor()
c.execute("INSERT INTO products values (001,'''Shirt''',2000,'''black T Shirt''',10,3)")
print(c.execute("SELECT * FROM products"))
con.close()