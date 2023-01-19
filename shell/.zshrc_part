################################################ recommended misc ################################################
# 1. ohmyzsh
# 2. zsh-syntax-highlighting zsh-autosuggestions
# 3. fzf
# 4. translate-shell
# 5. tldr
# 6. br

################################################ default settings ################################################
export ZSH="/Users/hongde/.oh-my-zsh"

ZSH_THEME="robbyrussell"

plugins=(git docker colored-man-pages golang colorize pip python brew macos zsh-syntax-highlighting zsh-autosuggestions minikube kubectl supervisor mvn helm rust)

source $ZSH/oh-my-zsh.sh

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

alias ls="ls --color=auto"
alias ll="ls -lh --color=auto"

# export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles
export HOMEBREW_NO_AUTO_UPDATE=1
export PATH="/Users/hongde/Library/Android/sdk/platform-tools:$PATH"
export ANDROID_HOME="/Users/hongde/Library/Android/sdk"
export HOMEBREW_NO_AUTO_UPDATE=true
export HOMEBREW_NO_INSTALL_CLEANUP=true

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
source /Users/hongde/.config/broot/launcher/bash/br

################################################ dev env settings ################################################
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home
export MAVEN_HOME=/Library/apache-maven-3.6.3
export PATH=$MAVEN_HOME/bin:$PATH
export GOPATH=/Users/hongde/go
export PATH=$GOPATH/bin:$PATH
export ANDROID_HOME=~/Library/Android/sdk
export PATH="/usr/local/opt/php@7.2/bin:$PATH"
export PATH="/usr/local/opt/php@7.2/sbin:$PATH"
export PATH="/usr/local/sbin:$PATH"
export PATH="$PATH:$HOME/.composer/vendor/bin"
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/php@7.1/bin:$PATH"
export PATH="/usr/local/opt/php@7.1/sbin:$PATH"
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"

################################################ proxy settings ################################################
# GFW proxy
PROXY="http://127.0.0.1:7890"
alias proxy-on="export HTTP_PROXY=$PROXY; export HTTPS_PROXY=$PROXY; export ALL_PROXY=$PROXY; export http_proxy=$PROXY; export https_proxy=$PROXY;"
# debug proxy
DEBUG_PROXY="http://127.0.0.1:8090"
alias debug-proxy-on="export HTTP_PROXY=$DEBUG_PROXY; export HTTPS_PROXY=$DEBUG_PROXY; export ALL_PROXY=$DEBUG_PROXY; export http_proxy=$DEBUG_PROXY; export https_proxy=$DEBUG_PROXY;"
# unset proxy settings
alias proxy-off="unset HTTP_PROXY; unset http_proxy; unset HTTPS_PROXY; unset https_proxy; unset ALL_PROXY"
# for kubernetes ip 
export NO_PROXY=localhost,127.0.0.1,10.96.0.0/12,192.168.99.0/24,192.168.39.0/24,192.168.64.2

################################################ shell helper ################################################
alias ipaddr="echo $(ifconfig | grep broadcast | awk '{ print $2 }')"
alias transs='transs(){ proxy-on; trans $@; proxy-off;}; transs'
alias transz='transz(){ proxy-on; trans zh:en $@; proxy-off;}; transz'
alias transe='transe(){ proxy-on; trans en:zh $@; proxy-off;}; transe'
alias proxy-wrap='proxy-wrap(){ proxy-on; $@; proxy-off;}; proxy-wrap'
alias t2d='t2d() {date -d @$@ +"%Y-%m-%d %H:%M:%S"}; t2d'
alias dict='f(){ open "dict://${1}"; unset -f f; }; f'

################################################ dev data source ################################################
# copy from another private repo