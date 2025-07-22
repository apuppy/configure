```shell
docker build --progress=plain -t my-img -f toolkit-Dockerfile .
```

```shell
docker run -dit --name my-box my-img /bin/zsh
# expicit LANG env
docker run -dit --name my-box -e LANG=C.UTF-8 my-img /bin/zsh
```

```shell
docker exec -it my-box zsh
# expicit LANG env
docker exec -it -e LANG=C.UTF-8 my-box zsh
```

```shell
docker stop my-box
docker rm my-box
```

## TODO
- [x] translate-shell
- [x] tldr
- [x] oh-my-zsh & zsh-autosuggestions & zsh-syntax-highlighting