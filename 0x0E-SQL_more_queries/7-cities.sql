-- Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on my MySQL server.
--  If the database hbtn_0d_usa already exists, my script should not fail.
--  If the table cities already exists, your script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
id INT AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES states(id));
