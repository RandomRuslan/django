sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database QA_SQL"
sudo ./ask/manage.py makemigrations
sudo ./ask/manage.py migrate

