class DefaultConfig(object):
    DEBUG = True

    LOG_LEVEL = 'DEBUG'
    # Log file path
    # LOG_FILE='/app/logs/server.log'
    LOG_FILE = 'logs/app.log'
    # Log file max size, the unit is MB
    LOG_FILE_MAX_SIZE = 20
    # Log file max backup count
    LOG_FILE_BACKUP_COUNT = 5
    # Log dateformat
    LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
    # Log Timezone 'UTC'
    LOG_TZ = "Asia/Shanghai"
    # Log format
    LOG_FORMAT = '%(asctime)s,%(msecs)d %(levelname)-2s [%(filename)s:%(lineno)d] %(req_id)s %(message)s'

    # CORS configuration TODO 这里可能是列表形式 目前我看到的是列表和这种格式的字符串都可以
    WEB_API_CORS_ALLOW_ORIGINS = 'http://127.0.0.1:3000,*'
    CONSOLE_CORS_ALLOW_ORIGINS = 'http://127.0.0.1:3000,*'

    # sqlalchemy
    # pip install flask-sqlalchemy
    # pip install psycopg2-binary  # 如果使用PostgreSQL
    # pip install pymysql          # 如果使用MySQL
    # pip install sqlite           # SQLite通常内置
    # sqlite:///example.db
    # mysql+pymysql://username:password@host:port/database?charset=utf8mb4  # 支持 emoji 和更多字符
    # postgresql+psycopg2://username:password@host:port/database?client_encoding=utf8  # 默认是utf8
    DB_USERNAME = 'goboy'
    DB_PASSWORD = '123456'
    DB_HOST = 'localhost'
    DB_PORT = '13306'
    DB_DATABASE = 'ftest'
    DB_CHARSET = 'utf8mb4'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset={DB_CHARSET}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True  # 是否显示SQLAlchemy生成的SQL语句 这玩意非必要情况，别开，太多废话了
    # SQLALCHEMY_POOL_SIZE = 10  # 连接池的大小，默认是5
    # SQLALCHEMY_MAX_OVERFLOW = 20  # 连接池中最多可以创建的连接数，默认是10
    # SQLALCHEMY_POOL_TIMEOUT = 30  # 连接池中连接的超时时间，默认是30秒
    # SQLALCHEMY_POOL_RECYCLE = 1800  # 连接池中连接的回收时间，默认是1800秒
    # SQLALCHEMY_BINDS  # 连接多个数据库  https://docs.jinkan.org/docs/flask-sqlalchemy/binds.html

    # 配置Redis连接
    REDIS_HOST = 'localhost'
    REDIS_PORT = 16379
    REDIS_DB = 0
    REDIS_PASSWORD = None  # 如果没有密码则为 None

    # celery
    # redis://:password@host:port/db
    # redis://localhost:16379/0
    CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
    '''
    # CELERY_RESULT_BACKEND = 'redis://localhost:16379/0'
    
    # sqlite (filename)
    result_backend = 'db+sqlite:///results.sqlite'

    # mysql
    result_backend = 'db+mysql://scott:tiger@localhost/foo'

    # postgresql
    result_backend = 'db+postgresql://scott:tiger@localhost/mydatabase'

    # oracle
    result_backend = 'db+oracle://scott:tiger@127.0.0.1:1521/sidname'
    '''
    CELERY_BACKEND = 'database'  # 4.x开始弃用
    CELERY_RESULT_BACKEND = f'db+mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
    CELERY_BEAT_SCHEDULER_TIME = 1
