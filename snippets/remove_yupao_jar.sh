#!/bin/bash
# maven拉依赖未更新到最新版本时，尝试删除本地maven依赖文件
rm -rf $HOME/.m2/repository/com/yp
rm -rf $HOME/.m2/repository/com/yupao