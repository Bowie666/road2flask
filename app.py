import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    # TODO flask 有好几种配置文件的方式 以后慢慢添加
    app.config.from_object(config)
    # app.config.from_mapping(dify_config.model_dump())  # 这个方法是接收一个字典

    # 这段代码的目的是将 Flask 配置中的每个项都同步到系统环境变量中。用于需要访问环境变量的场景，尤其是用于多环境部署时
    # 可以在开发环境、测试环境和生产环境之间切换，只需要通过环境变量来传递配置。
    # populate configs into system environment variables
    for key, value in app.config.items():
        if isinstance(value, str):
            os.environ[key] = value
        elif isinstance(value, int | float | bool):
            os.environ[key] = str(value)
        elif value is None:
            os.environ[key] = ""

    return app

