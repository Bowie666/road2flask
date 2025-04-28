from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger


scheduler = BackgroundScheduler()

def my_cron_job():
    try:
        print('Hello from my job!')
        # 在此处添加实际的任务逻辑
    except Exception as e:
        print(f'Error executing cron job: {e}')


def init_app(app: Flask):
    # 配置任务
    scheduler.add_job(
        func=my_cron_job,
        # trigger=CronTrigger(hour=9, minute=30),
        trigger = IntervalTrigger(seconds=2),  # 任务每2秒执行一次
        id='my_cron_job',  # 给任务指定唯一的 ID，方便后期管理
    )

    # 启动调度器
    scheduler.start()
