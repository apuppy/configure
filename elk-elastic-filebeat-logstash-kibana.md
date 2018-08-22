#### filebeat
```
filebeat.inputs:
- input_type: log
  paths:
    - /var/log/nginx/access.log
  document_type: nginx_access_log
  tags: ["nginx-accesslog"]
output.logstash:
    hosts: ["localhost:5044"]
# nginx access_log format
    log_format  main  "$time_local | $remote_addr | $http_host | $http_x_forwarded_for | $request_method | $request_uri | $server_protocol | $status | $body_bytes_sent | $http_referer | $http_user_agent | $request_time |";
```



#### logstash
```

# /etc/logstash/conf.d/nginx_access.conf

input {
    beats {
        port => 5044
    }   
}

filter {
    if "nginx_accesslog" in [tags] {
        grok {
             match => { "message" => "%{HTTPDATE:timestamp}\|%{IP:remote_addr}\|%{IPORHOST:http_host}\|(?:%{DATA:http_x_forwarded_for}|-)\|%{DATA:request_method}\|%{DATA:request_uri}\|%{DATA:server_protocol}\|%{NUMBER:status}\|(?:%{NUMBER:body_bytes_sent}|-)\|(?:%{DATA:http_referer}|-)\|%{DATA:http_user_agent}\|(?:%{DATA:request_time}|-)\|"}
        }
        mutate {
            convert => ["status","integer"]
            convert => ["body_bytes_sent","integer"]
            convert => ["request_time","float"]
        }
        geoip {
            source => "remote_addr"
        }
        date {
            match => ["timestamp","dd/MM/YYYY:HH:mm:ss Z"] 
        }
        useragent {
            source => "http_user_agent"
        }
    }   
}

output {
    elasticsearch {
        hosts => ["127.0.0.1:9200"]
        index => "logstash-%{type}-%{+YYYY.MM.dd}"
        document_type => "%{type}"
    }   
    stdout { codec => rubydebug }
}
```




systemctl start elasticsearch

systemctl start kibana

systemctl start logstash
// logstash -t -f /etc/logstash/conf.d/nginx_access.conf

systemctl start filebeat
