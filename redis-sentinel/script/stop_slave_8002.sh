#!/bin/sh
ps -ef | grep 8002 | grep -v grep | awk '{print$2}' | xargs kill
