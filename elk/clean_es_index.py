# -*- coding: utf-8 -*-
# requests library : pip install requests
# curl -s --user elastic:elastic_admin -XGET localhost:9200 | jq .
# curl -s --user elastic:elastic_admin -XGET "http://localhost:9200/_cat/indices?v&s=store.size"
import datetime
import sys
import time

import requests

ELASTIC_HOST = "http://127.0.0.1:9200"
ELASTIC_USER = "elastic"
ELASTIC_PASSWORD = "elastic_admin"

DELETE_INDEX_MATCH = ["filebeat-", ".monitoring-es", ".monitoring-kibana"]
EXPIRATION_DAYS_AGO = 5


# get indexes from the elasticsearch node
def get_indexes(elastic_host):
    # r = requests.get(elastic_host + '/_cat/indices?v&h=h,s,i,id,dc,ss,creation.date.string,creation.date')
    r = requests.get(elastic_host + '/_cat/indices?v&h=h,s,i,id,dc,ss,creation.date.string,creation.date',
                     auth=(ELASTIC_USER, ELASTIC_PASSWORD))
    index_rows = []
    lines = r.text.splitlines()
    lines.pop(0)
    for line in lines:
        fields = line.split()
        create_timestamp = int(fields[7]) / 1000
        index_row = {"idx_name": fields[2], "storage_size": fields[5], "idx_create_datetime": fields[6],
                     "idx_create_timestamp": create_timestamp}
        index_rows.append(index_row)
    return index_rows


# finally delete the index
def delete_expired_index(index):
    # print("delete index [ " + index['idx_name'] + " ] [" + index['idx_create_datetime'] + "] [storage_size]")
    elastic_host = get_elastic_host()
    # r = requests.delete(elastic_host + '/' + index['idx_name'])
    r = requests.delete(elastic_host + '/' + index['idx_name'], auth=(ELASTIC_USER, ELASTIC_PASSWORD))
    if r.status_code == 200:
        return True
    else:
        return False


# get current datetime
def get_now_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# show confirm dailog in interactive mode in command line
def show_confirm_dialog(index):
    delete_flag = False
    answer = input(
        "Are you sure to delete index: [ " + index['idx_name'] + " ] [" + index['idx_create_datetime'] + "] [" + index[
            'storage_size'] + "], type yes|y or no|n ")
    if answer == "yes" or answer == 'y':
        delete_flag = True
    elif answer == "no" or answer == 'n':
        pass
    else:
        pass
    return delete_flag


# interactive mode or not
def is_interactive_mode():
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    # args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    if "--non-interactive" in opts:
        return False
    else:
        return True


# check if index is expired
def check_if_index_expired(index_create_timestamp, expiration_timestamp):
    if index_create_timestamp < expiration_timestamp:
        return True
    else:
        return False


# get expiration timestamp
def get_expired_deadline():
    days_ago = (datetime.datetime.now() - datetime.timedelta(days=EXPIRATION_DAYS_AGO))
    timestamp = int(time.mktime(days_ago.timetuple()))
    ymd_datetime = days_ago.strftime("%Y-%m-%d %H:%M:%S")
    return {"datetime": ymd_datetime, "timestamp": timestamp}


# check if index match delete index match rules
def check_index_match_delete_rules(index_name):
    match = False
    for rule in DELETE_INDEX_MATCH:
        if index_name.startswith(rule):
            match = True
    return match


# get elasticsearch host
def get_elastic_host():
    if ELASTIC_HOST.endswith("/"):
        elastic_host = ELASTIC_HOST[:-1]
    else:
        elastic_host = ELASTIC_HOST
    return elastic_host


# entry point
def main():
    elastic_host = get_elastic_host()
    indexes = get_indexes(elastic_host)  # 取出所有索引
    deadline = get_expired_deadline()
    for index in indexes:
        matched = check_index_match_delete_rules(index['idx_name'])  # 是否匹配要删除的索引名
        if not matched: continue
        expired = check_if_index_expired(index['idx_create_timestamp'], deadline['timestamp'])  # 索引是否已过失效期
        if not expired: continue
        interactive = is_interactive_mode()  # 是否是交互模式，交互模式需要确认，默认为交互模式，--non-interactive取消交互模式
        if interactive:
            confirmed = show_confirm_dialog(index)
            if not confirmed: continue
        deleted = delete_expired_index(index)
        if deleted:
            now_datetime = get_now_datetime()
            print("Index deleted at {0}: [ {1} ] [{2}] [{3}]".format(now_datetime, index['idx_name'],
                                                                     index['idx_create_datetime'],
                                                                     index['storage_size']))


""" ------------ call entry point ------------ """

main()
