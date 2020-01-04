-- Creates the database hbnb_dev_db in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates the MySQL server user hbnb_dev.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant Privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db. * TO 'hbnb_dev'@'localhost';
-- Creates schema performance_schema in your MySQL server.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush
FLUSH PRIVILEGES;