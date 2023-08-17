import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
dolls = [
    (1, "Zero", "Fashion Doll", 0, "First Doll"),
                                (2,"Barbie", "Fashion Doll", 100, "The first doll"),
                                (3, "Ken", "Fashion Doll", "75", "Rockstar Ken"),
                                (4, "Skipper", "Fashion Doll", "50", "Barbie's sister"),
                                (5, "Stacie", "Fashion Doll", "50", "Barbie's sister"),
                                (6, "Chelsea", "Fashion Doll", "50", "Barbie's sister"),
                                (7, "Teresa", "Fashion Doll", "50", "Barbie's friend"),
                                (8, "Christie", "Fashion Doll", "50", "Barbie's friend"),
                                (9, "Michelle", "Fashion Doll", "50", "Barbie's friend"),
                                (10, "Nikki", "Fashion Doll", "50", "Barbie's friend"),
                                (11, "Raquelle", "Fashion Doll", "50", "Barbie's friend"),
                                (12, "Ryan", "Fashion Doll", "50", "Barbie's friend"),
                                (13, "Steven", "Fashion Doll", "50", "Barbie's friend"),
                                (14, "Blaine", "Fashion Doll", "50", "Barbie's friend"),
                                (15, "Summer", "Fashion Doll", "50", "Barbie's friend"),
                                (16, "Cindy", "Fashion Doll", "50", "Barbie's friend"),
                                (17, "Tutti", "Fashion Doll", "50", "Barbie's friend"),
                                (18, "Todd", "Fashion Doll", "50", "Barbie's friend"),
                                (19, "Linda", "Fashion Doll", "50", "Barbie's friend")
]
cur.executemany("INSERT INTO Doll (id, name, type, price, details) VALUES (?,?,?,?,?)", dolls)

connection.commit()
connection.close()