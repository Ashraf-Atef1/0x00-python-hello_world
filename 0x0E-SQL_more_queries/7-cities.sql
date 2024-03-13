-- a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
CREATE TABLE IF NOT EXIST hbtn_0d_usa.cities(
  id INT UNIQUE AUTO-INCREMENT NOT NULL PRIMARY KEY,
  FOREIGN KEY(state_id) REFERENCES states(id),
  name VARCHAR(256) NOT NULL
);
