#### php yii2 redis queue配置
```php
return [
    'bootstrap' => [
        'queue', // 把这个组件注册到控制台
    ],
    'components' => [
        'redis' => [
            'class' => \yii\redis\Connection::class,
            // ...
        ],
        'queue' => [
            'class' => \yii\queue\redis\Queue::class,
            'redis' => 'redis', // 连接组件或它的配置
            'channel' => 'queue', // Queue channel key
        ],
    ],
];
```

#### 控制台操作
listen 启动守护进程队列，无限循环并处理列队里的内容,有新任务会立即被消费。
[timeout] 是下一次查询队列的时间 当命令正确地通过supervisor来实现时，这种方法最有效。
```bash
# yii queue_name/listen [timeout]
yii queue/listen [timeout]
```
run 命令获取并执行循环中的任务，直到队列为空，适用于linux 定时任务，例如cron
```bash
# yii queue_name/run
yii queue/run
```
run 与 listen 命令的参数:
	--verbose, -v: 将执行状态输出到控制台。
	--isolate: 详细模式执行作业。如果启用，将打印每个作业的执行结果。
	--color: 高亮显示输出结果。

info 命令打印关于队列状态的信息。
```bash
yii queue/info
```
清除队列
```bash
yii queue/clear
```
删除task
```bash
yii queue/remove [id]
```

#### 结合supervisor工作
supervisor配置一个任务
```bash
[program:yii-queue-worker]
process_name=%(program_name)s_%(process_num)02d
command=/usr/bin/php /var/www/my_project/yii queue/listen --verbose=1 --color=0
autostart=true
autorestart=true
user=www-data
numprocs=4
redirect_stderr=true
stdout_logfile=/var/www/my_project/log/yii-queue-worker.log
```