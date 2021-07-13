-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on my MySQL server.
--  id with the default value 1 must be unique, can’t be null and is a primary key.
--  If the table states already exists, my script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL);
