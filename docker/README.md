```shell
docker build --progress=plain -t my-img -f toolkit-Dockerfile .
```

```shell
docker run -dit --name my-box my-img /bin/zsh
```

```shell
docker exec -it my-box zsh
```

```shell
docker stop my-box
docker rm my-box
```

## TODO
- [ ] translate-shell
- [ ] tldr
- [ ] oh-my-zsh & zsh-autosuggestions & zsh-syntax-highlighting