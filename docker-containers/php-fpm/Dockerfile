FROM php:7.2-fpm
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mv /etc/apt/sources.list /etc/apt/sources.list.backup && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" > /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free" >> /etc/apt/sources.list \
	&& php -m \
    && docker-php-ext-install pdo_mysql \
	&& pecl install redis \
	&& docker-php-ext-enable redis \
    && php -m
COPY ./config/* /usr/local/etc/php/conf.d/
COPY . /var/www/html
WORKDIR /var/www/html
# CMD [ "php", "./index.php" ]
CMD ["php-fpm"]
EXPOSE 9000
