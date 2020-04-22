# change $HOME/data/redis to the folder path where you would like in host
# port mapping 6379
docker run --name some-redis -v $HOME/data/redis:/data -p 6379:6379 -d redis redis-server --appendonly yes