-- Creates the database hbnb_dev_db with specified paramenters
CREATE DATABASE IF NOT EXISTS 'hbnb_test_db';
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON 'hbnb_test_db'.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT PRIVILEGES ON 'performance_schema'.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES