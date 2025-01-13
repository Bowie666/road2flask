# road2flask
i want to use flask clarity


## structure
```
├── apps        # 放接口吧 先简单点 下面的结构分支先不动 等以后在修改
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates
│       ├── index.html
│       └── layout.html
├── models          # 模型文件
├── extensions      # 扩展
│   ├── ext_blueprint.py        # 蓝图的配置
│   ├── ext_celery.py           # celery的配置 这里有点问题 就是看不到celery的运行状态 老是pending 数据库也看不到
│   ├── ext_db.py               # 数据库的配置
│   ├── ext_logging.py          # 日志的配置
│   ├── ext_migrate.py          # 迁移的配置
│   └── ext_redis.py            # redis的配置
├── configs.py                  # 先把配置文件放着 可以把这一块抽成文件夹
├── requirements.txt            # python依赖
├── app.py                      # 入口
└── commands.py                 # 命令行代码 自定义初始化命令
```

## tips
- 由于flask性能不足，一般配合下面的工具一起使用
  - Nginx：高性能 Web 服务器+负载均衡；
  - gunicorn：高性能 WSGI 服务器；
  - gevent：把 Python 同步代码变成异步协程的库；
  - Supervisor：监控服务进程的工具；

##### reference
- dify
