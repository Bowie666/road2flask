import time

from celery import shared_task


# 定义一个 Celery 异步任务
# @celery.task 需要显式地通过 celery.task 方法绑定到某个 Celery 实例
@shared_task  # 不需要绑定到实例 谁都能用
def long_task():
    time.sleep(20)  # 模拟耗时操作
    return 'Task completed!'
