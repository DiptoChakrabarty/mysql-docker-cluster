CREATE USER 'clusteradmin'@'%' IDENTIFIED BY 'cladmin';

GRANT ALL privileges ON *.* TO 'clusteradmin'@'%' with grant option;

FLUSH PRIVILEGES;