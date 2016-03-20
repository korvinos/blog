# Создаем базу данных MySQL
mysql -uroot -e "CREATE DATABASE my_blog;"
mysql -uroot -e "CREATE USER 'korvinos'@'localhost' IDENTIFIED BY '1234';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON my_blog.* TO 'korvinos'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
