-- Create a new database
CREATE DATABASE mydb;

-- Connect to the new database
\c mydb;

-- Create a sample table
CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL
);

-- Insert a test row
INSERT INTO test_table (message) VALUES ('Hello from Postgres!');
