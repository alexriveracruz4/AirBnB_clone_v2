-- Creates the database hbnb_dev_db with specified paramenters
-- Set ALL privileges on the database hbnb_dev_db to the hbnb_dev user.
-- Set SELECT privileges on the database performance_schema to the hbnb_dev user.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
