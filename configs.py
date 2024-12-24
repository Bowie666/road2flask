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

