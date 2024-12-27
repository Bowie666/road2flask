import redis
from flask import Flask

from configs import DefaultConfig


def init_app(app: Flask):
    # 创建Redis连接池
    redis_pool = redis.ConnectionPool(
        host=DefaultConfig.REDIS_HOST, 
        port=DefaultConfig.REDIS_PORT, 
        db=DefaultConfig.REDIS_DB, 
        password=DefaultConfig.REDIS_PASSWORD,
        decode_responses=True  # 默认将返回的值解码为字符串
    )

    # 创建Redis客户端
    redis_client = redis.Redis(connection_pool=redis_pool)

    # 这里最好改个名叫cache 如果后期要换memcache之类的 全都得改
    # 如果起名叫redis 以后想用memcache还得改代码 如果叫cache 就只改这里就行
    app.extensions["redis"] = redis_client


'''
from flask import current_app

# 使用 current_app 获取当前应用实例
def get_cache(key):
    redis_client = current_app.extensions["redis"]  # 从 current_app 获取 redis 客户端

    redis_client.set(key, value)
    value = redis_client.get(key)
    result = redis_client.delete(key)
'''
