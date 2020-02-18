#### logstash 测试运行
```
# 测试
sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/main.conf -t
# 运行
sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/main.conf
```

#### filebeat 测试运行
```
sudo filebeat test config
```

#### filebeat开启内置模块
```
sudo filebeat modules list
sudo filebeat enable nginx
sudo filebeat setup -e
# 临时禁用logstash : output.logstash.enabled=false
sudo filebeat setup -e \
  -E output.logstash.enabled=false \
  -E output.elasticsearch.hosts=['localhost:9200'] \
  -E output.elasticsearch.username=filebeat_internal \
  -E output.elasticsearch.password=YOUR_PASSWORD \
  -E setup.kibana.host=localhost:5601

# 连接ES,同步filebeat内置模块的日志解析配置
sudo filebeat setup -e \
  -E output.logstash.enabled=false \
  -E output.elasticsearch.hosts=['localhost:9200'] \
  -E output.elasticsearch.username=filebeat_internal \
  -E output.elasticsearch.password=YOUR_PASSWORD \
  -E setup.kibana.host=localhost:5601
  --pipelines --modules nginx,apache2
```
