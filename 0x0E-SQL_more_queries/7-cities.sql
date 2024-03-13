-- a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
CREATE TABLE IF NOT EXIST hbtn_0d_usa.cities(
  id INT UNIQUE AUTO-INCREMENT NOT NULL PRIMARY KEY,
  state_id INT FOREIGN KEY REFERENCES states(id),
  name VARCHAR(256) NOT NULL
);
