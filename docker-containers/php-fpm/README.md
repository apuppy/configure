## build
```
docker build -t image-php-fpm .
```
## run
```
docker run -d --rm --name php-fpm image-php-fpm
```
## interactive shell to php-fpm container
```
docker exec -it php-fpm bash
```
## stop & start
```
docker stop php-fpm
docker start php-fpm # when run without -d
```