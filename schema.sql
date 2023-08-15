DROP TABLE IF EXISTS Doll;

CREATE TABLE Doll (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    price FLOAT CHECK (price >= 0) NOT NULL,
    details TEXT NOT NULL
);