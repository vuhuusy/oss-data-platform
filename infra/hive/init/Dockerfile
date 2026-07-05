FROM apache/hive:standalone-metastore-4.2.0

# Set working directory
WORKDIR /opt/hive/lib

# Download PostgreSQL JDBC driver
ADD https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.3/postgresql-42.7.3.jar .

USER root
