-- Script that creates a table users
-- id: integer, never null, auto_increment and primary key
-- email: string(255 characters), never null and unique
-- name: string(255 characters)
-- country: enumaration of countries: US, CO AND TN, never null

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);