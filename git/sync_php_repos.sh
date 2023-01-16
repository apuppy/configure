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
"log-service"
"marketing-service"
"message-service"
"pay-service"
"recruitment_main_station"
"risk-service"
"user-data"
"user-service"
)

for repo in ${repos[@]}
do
	full_repo_path="/Users/hongde/code/work/php/$repo"
	echo $full_repo_path
	cd $full_repo_path && git pull && git checkout prod
done
