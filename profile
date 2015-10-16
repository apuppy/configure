# /etc/profile
# 
# add these configure options into /etc/profile if necessary
#

#java environment
JAVA_HOME=/usr/local/jdk
PATH=$PATH:$JAVA_HOME/bin
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
# python
PATH=$PATH:/usr/local/python34/bin
export PATH
# PHP
PATH=$PATH:/usr/local/php/bin
export PATH
#MariaDB
PATH=$PATH:/usr/local/mariadb/bin
# redis
PATH=$PATH:/usr/local/redis/bin
export PATH
# apache
PATH=$PATH:/usr/local/apache2/bin
export PATH
# nginx
PATH=$PATH:/usr/local/nginx/sbin
export PATH
# nodejs
PATH=$PATH:/usr/local/node/bin
export PATH
