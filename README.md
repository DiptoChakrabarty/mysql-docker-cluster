# mysql-docker-cluster

Setup a three node mysql innodb cluster using docker containers in any system.

## Steps to run

- Start the docker containers
```
docker-compose up
or
docker-compose up -d
```

- Check if three containers are running
```
docker ps
```

- In each mysql node a clusteradmin user is created with super user privileges

- To configure another user or change password modify username and password in setup.sql file

- To change root password change in compose file directly