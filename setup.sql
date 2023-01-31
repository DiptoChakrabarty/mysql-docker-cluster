CREATE USER inno@localhost IDENTIFIED BY 'inno';

GRANT ALL privileges ON *.* TO inno@localhost with grant option;

FLUSH PRIVILEGES;