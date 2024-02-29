#!/bin/sh
ps -ef | grep 8000 | grep -v grep | awk '{print$2}' | xargs kill
