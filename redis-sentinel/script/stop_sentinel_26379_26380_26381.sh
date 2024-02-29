#!/bin/sh
echo "将要停止的redis sentinel 进程 Id 如下..."
ps -ef | grep sentinel | grep -v grep | grep -v stop_sentinel_26379_26380_26381 | awk '{print $2}'

echo "将要停止redis sentinel......"
pids=$(ps -ef | grep sentinel | grep -v grep | awk '{print $2}')
for pid in $pids; do
  echo "kill $pid"
  kill $pid
done

