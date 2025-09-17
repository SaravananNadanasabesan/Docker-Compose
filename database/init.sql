CREATE DATABASE testdb;

\c testdb

CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL
);

INSERT INTO test_table (message) VALUES ('Hello from Postgres!');
