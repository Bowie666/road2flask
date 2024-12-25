import logging

from flask_restful import Resource


# 常用的蓝图代码结构
class HelloResource(Resource):
    def get(self):
        logging.info('hello world')
        return {'hello': 'world'}

    def post(self):
        return {'msg': 'post hello world'}

