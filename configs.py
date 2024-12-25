class DefaultConfig(object):
    DEBUG = True

    LOG_LEVEL = 'DEBUG'
    # Log file path
    # LOG_FILE='/app/logs/server.log'
    LOG_FILE = 'logs/app.log'
    # Log file max size, the unit is MB
    LOG_FILE_MAX_SIZE=20
    # Log file max backup count
    LOG_FILE_BACKUP_COUNT=5
    # Log dateformat
    LOG_DATEFORMAT='%Y-%m-%d %H:%M:%S'
    # Log Timezone "Asia/Shanghai"
    LOG_TZ='UTC'
    # Log format
    LOG_FORMAT='%(asctime)s,%(msecs)d %(levelname)-2s [%(filename)s:%(lineno)d] %(req_id)s %(message)s'

    # CORS configuration TODO 这里可能是列表形式 目前我看到的是列表和这种格式的字符串都可以
    WEB_API_CORS_ALLOW_ORIGINS='http://127.0.0.1:3000,*'
    CONSOLE_CORS_ALLOW_ORIGINS='http://127.0.0.1:3000,*'
