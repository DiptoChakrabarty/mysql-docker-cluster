FROM mysql/mysql-server:8.0

COPY ./setup.sql /docker-entrypoint-initdb.d

EXPOSE 3306