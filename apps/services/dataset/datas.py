import logging

from flask_restful import Resource

from apps.services import services_api
from models.data import Data
from extensions.ext_db import db


# 常用的蓝图代码结构
class HelloDataResource(Resource):
    def get(self):
        logging.info('hello data')
        return {'hello': 'data'}

    def post(self):
        data = Data(
            name='hello'
        )
        try:
            db.session.add(data)
            db.session.commit()
            logging.info('post success')
        except Exception as e:
            db.session.rollback()
            logging.error(e)
        
        return {'msg': 'post hello data'}
    

services_api.add_resource(HelloDataResource, '/data')
