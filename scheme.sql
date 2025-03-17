CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE,
    password VARCHAR
);

INSERT INTO users (username, password) VALUES
      ("root", "root"),
      ("user", "user"),
      ("test", "test");