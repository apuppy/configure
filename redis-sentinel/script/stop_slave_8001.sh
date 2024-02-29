#!/bin/sh
ps -ef | grep 8001 | grep -v grep | awk '{print$2}' | xargs kill
