from flask import Blueprint
from flask_restful import Api

from .core_api import HelloResource


# 如果用这种方法 必须在这里注册函数
services_bp = Blueprint("services", __name__, url_prefix="/services/api")
services_api = Api(services_bp)

services_api.add_resource(HelloResource, '/')


# 如果是文件夹结构 必须把文件名引过来才可以注册 真麻烦
from .dataset import datas

