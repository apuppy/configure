```shell
docker build --progress=plain -t my-img -f toolkit-Dockerfile .
```

```shell
docker run -dit --name my-box -e LANG=C.UTF-8 my-img /bin/zsh
```

```shell
docker exec -it -e LANG=C.UTF-8 my-box zsh
```

```shell
docker stop my-box
docker rm my-box
```

## TODO
- [ ] translate-shell
- [ ] tldr
- [ ] oh-my-zsh & zsh-autosuggestions & zsh-syntax-highlighting