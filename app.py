import os

from flask import Flask

from configs import DefaultConfig

def create_app():
    app = Flask(__name__)
    # TODO flask 有好几种配置文件的方式 以后慢慢添加
    app.config.from_object(DefaultConfig)
    # app.config.from_mapping(dify_config.model_dump())  # 这个方法是接收一个字典

    # 这段代码的目的是将 Flask 配置中的每个项都同步到系统环境变量中。用于需要访问环境变量的场景，尤其是用于多环境部署时
    # 可以在开发环境、测试环境和生产环境之间切换，只需要通过环境变量来传递配置。
    # populate configs into system environment variables
    for key, value in app.config.items():
        if isinstance(value, str):
            os.environ[key] = value
        # elif isinstance(value, int | float | bool):
        elif isinstance(value, (int, float, bool)):
            os.environ[key] = str(value)
        elif value is None:
            os.environ[key] = ""

    return app

'''
# 看一下python版本是否合规
import sys


def check_supported_python_version():
    python_version = sys.version_info
    if not ((3, 11) <= python_version < (3, 13)):
        print(
            "Aborted to launch the service "
            f" with unsupported Python version {python_version.major}.{python_version.minor}."
            " Please ensure Python 3.11 or 3.12."
        )
        raise SystemExit(1)
'''

# 看情况用哪个 这个是用gevent
if not DefaultConfig.DEBUG:
    from gevent import monkey
    from grpc.experimental import gevent as grpc_gevent

    # gevent
    monkey.patch_all()

    # grpc gevent
    grpc_gevent.init_gevent()



def initialize_extensions(app: Flask):
    import logging
    import time

    from extensions import (
        ext_blueprints,
        ext_db,
        ext_logging,
        ext_migrate,
        # ext_app_metrics,
        # ext_celery,
        # ext_code_based_extension,
        # ext_commands,
        # ext_compress,
        # ext_hosting_provider,
        # ext_import_modules,
        # ext_login,
        # ext_mail,
        # ext_proxy_fix,
        # ext_redis,
        # ext_sentry,
        # ext_set_secretkey,
        # ext_storage,
        # ext_timezone,
        # ext_warnings,
    )

    extensions = [
        ext_blueprints,
        ext_db,
        ext_logging,
        ext_migrate,
        # ext_timezone,
        # ext_warnings,
        # ext_import_modules,
        # ext_set_secretkey,
        # ext_compress,
        # ext_code_based_extension,
        # ext_app_metrics,
        # ext_redis,
        # ext_storage,
        # ext_celery,
        # ext_login,
        # ext_mail,
        # ext_hosting_provider,
        # ext_sentry,
        # ext_proxy_fix,
        # ext_commands,
    ]
    for ext in extensions:
        short_name = ext.__name__.split(".")[-1]
        is_enabled = ext.is_enabled() if hasattr(ext, "is_enabled") else True
        if not is_enabled:
            if DefaultConfig.DEBUG:
                logging.info(f"Skipped {short_name}")
            continue

        start_time = time.perf_counter()
        ext.init_app(app)
        end_time = time.perf_counter()
        if DefaultConfig.DEBUG:
            logging.info(f"Loaded {short_name} ({round((end_time - start_time) * 1000, 2)} ms)")


# create app
app = create_app()
initialize_extensions(app)
# celery = app.extensions["celery"]


@app.route('/url_map')
def route_map():
    """
    主视图，返回所有视图网址
    """
    rules_iterator = app.url_map.iter_rules()
    return {rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
