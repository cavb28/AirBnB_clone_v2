-- Creates the database hbnb_dev_db in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates the MySQL server user hbnb_dev.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant Privileges
GRANT ALL PRIVILEGES ON hbnb_test_db. * TO 'hbnb_test'@'localhost';
-- Creates schema performance_schema in your MySQL server.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flush
FLUSH PRIVILEGES;
