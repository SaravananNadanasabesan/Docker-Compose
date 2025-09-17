# Use the official PostgreSQL image (version 13) as the base image
FROM postgres:13

# Copy the SQL initialization script into the special directory
# Any scripts in this folder will be automatically executed by the Postgres container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default PostgreSQL port so other containers can connect to the database
EXPOSE 5432