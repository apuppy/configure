#!/bin/bash

repos=(
	"advert-service"
	"authority-service"
	"backend-service"
	"common-service"
	"crontab-messages"
	"crontab-service"
	"file-service"
	"job_commom"
	"job-business"
	"login-service"
	"logger"
	"log-service"
	"marketing-service"
	"message-service"
	"pay-service"
	"recruitment_main_station"
	"risk-service"
	"user-data"
	"user-service"
)

repo_parent_dir="/Users/hongde/code/work/php/"

for repo in ${repos[@]}; do
	full_repo_path=$repo_parent_dir$repo
	echo $full_repo_path
	if [[ $repo = "logger" ]]; then
		cd $full_repo_path && git pull && git checkout release-2.0
	elif [[ $repo = "crontab-message" ]]; then
		cd $full_repo_path && git pull && git checkout master
	else
		cd $full_repo_path && git pull && git checkout prod
	fi
done
