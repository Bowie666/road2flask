from datetime import timedelta

import pytz
from flask import Flask
from celery import Celery, Task
from celery.schedules import crontab

from configs import DefaultConfig


'''
生成 Celery 数据库表时，应该直接运行任务而无需额外命令。SQLAlchemy 会自动创建表。

celery -A app.celery worker --loglevel=info
'''

def init_app(app: Flask) -> Celery:
    import pymysql
    pymysql.install_as_MySQLdb()

    # 确保任务在 Flask 应用上下文中执行，允许任务访问数据库等 Flask 上下文资源。
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)


    celery_app = Celery(
        app.name,
        task_cls=FlaskTask,
        broker=DefaultConfig.CELERY_BROKER_URL,
        # 是用于存储任务结果的后端。Celery 支持多种结果存储方式（例如数据库、Redis、RabbitMQ等）。这个配置项指定了存储任务结果的后端系统。
        # 如果任务需要返回结果，Celery 会将其存储在这个后端，并且可以在任务执行完成后从后端中获取结果。
        # backend=DefaultConfig.CELERY_BACKEND,  # 4.x开始弃用
        backend=DefaultConfig.CELERY_RESULT_BACKEND,
        task_ignore_result=True,  # 忽略任务的返回结果
    )

    celery_app.conf.update(
        result_backend=DefaultConfig.CELERY_RESULT_BACKEND,
        broker_connection_retry_on_startup=True,  # 连接重试 启动时自动重试连接到消息队列。
        worker_log_format=DefaultConfig.LOG_FORMAT,
        worker_task_log_format=DefaultConfig.LOG_FORMAT,
        worker_hijack_root_logger=False,
        timezone=pytz.timezone(DefaultConfig.LOG_TZ),
        task_track_started=True,  # 启用任务跟踪
    )

    if DefaultConfig.LOG_FILE:
        celery_app.conf.update(
            worker_logfile=DefaultConfig.LOG_FILE,
        )

    celery_app.set_default()  # 设置 Celery 应用的默认配置。

    app.extensions["celery"] = celery_app

    # imports = [
    #     "schedule.clean_embedding_cache_task",
    #     "schedule.clean_unused_datasets_task",
    #     "schedule.create_tidb_serverless_task",
    #     "schedule.update_tidb_serverless_status_task",
    #     "schedule.clean_messages",
    # ]
    # day = DefaultConfig.CELERY_BEAT_SCHEDULER_TIME
    # 定时任务
    # beat_schedule = {
    #     "clean_embedding_cache_task": {
    #         "task": "schedule.clean_embedding_cache_task.clean_embedding_cache_task",
    #         "schedule": timedelta(days=day),
    #     },
    #     "clean_unused_datasets_task": {
    #         "task": "schedule.clean_unused_datasets_task.clean_unused_datasets_task",
    #         "schedule": timedelta(days=day),
    #     },
    #     "create_tidb_serverless_task": {
    #         "task": "schedule.create_tidb_serverless_task.create_tidb_serverless_task",
    #         "schedule": crontab(minute="0", hour="*"),
    #     },
    #     "update_tidb_serverless_status_task": {
    #         "task": "schedule.update_tidb_serverless_status_task.update_tidb_serverless_status_task",
    #         "schedule": timedelta(minutes=10),
    #     },
    #     "clean_messages": {
    #         "task": "schedule.clean_messages.clean_messages",
    #         "schedule": timedelta(days=day),
    #     },
    # }
    # celery_app.conf.update(beat_schedule=beat_schedule, imports=imports)

    return celery_app
