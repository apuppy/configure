#!/bin/sh
redis-sentinel /Users/hongde/dev/redis-sentinel/sentinel/redis-sentinel-26379.conf &
redis-sentinel /Users/hongde/dev/redis-sentinel/sentinel/redis-sentinel-26380.conf &
redis-sentinel /Users/hongde/dev/redis-sentinel/sentinel/redis-sentinel-26381.conf &
