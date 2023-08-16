import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Doll (id, name, type, price, details) VALUES (?,?,?,?,?)",
                                (1, "Zero", "FashionDoll", 0.0, "First Doll")
                                )

connection.commit()
connection.close()