import logging

from flask_restful import Resource

from apps.services import services_api


# 常用的蓝图代码结构
class HelloDataResource(Resource):
    def get(self):
        logging.info('hello data')
        return {'hello': 'data'}

    def post(self):
        return {'msg': 'post hello data'}
    

services_api.add_resource(HelloDataResource, '/data')
