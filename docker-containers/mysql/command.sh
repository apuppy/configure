docker run --name some-mysql -p 3306:3306 -v /data/mysql/conf:/etc/mysql/conf.d -v /data/mysql/datadir:/var/lib/mysql -e mysql_root_password=123456 -d mysql:5.7
