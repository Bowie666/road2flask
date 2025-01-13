import os
import sys
import uuid
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, g, has_request_context

from configs import DefaultConfig


class RequestIdFilter(logging.Filter):
    # This is a logging filter that makes the request ID available for use in
    # the logging format. Note that we're checking if we're in a request
    # context, as we may want to log things before Flask is fully loaded.
    def filter(self, record):
        record.req_id = get_request_id() if has_request_context() else ""
        return True


def get_request_id():
    if getattr(g, "request_id", None):
        return g.request_id

    new_uuid = uuid.uuid4().hex[:10]
    g.request_id = new_uuid

    return new_uuid


def init_app(app: Flask):
    """
    支持文件和控制台双重日志输出，兼顾长期存储和实时调试。
    文件日志自动轮换，防止磁盘空间占用过多。
    控制台日志添加请求上下文信息，便于定位问题。
    高度灵活，通过 DefaultConfig 管理各项配置，便于调整。
    """
    log_handlers = []
    log_file = DefaultConfig.LOG_FILE
    # 如果 log_file 存在，说明需要将日志写入文件。
    if log_file:
        log_dir = os.path.dirname(log_file)
        os.makedirs(log_dir, exist_ok=True)
        log_handlers.append(
            RotatingFileHandler(
                filename=log_file,
                maxBytes=DefaultConfig.LOG_FILE_MAX_SIZE * 1024 * 1024,
                backupCount=DefaultConfig.LOG_FILE_BACKUP_COUNT,
            )
        )

    # Always add StreamHandler to log to console 配置控制台日志处理器
    sh = logging.StreamHandler(sys.stdout)
    # RequestIdFilter 是一个自定义日志过滤器，可以为每条日志记录附加请求 ID
    sh.addFilter(RequestIdFilter())
    log_formatter = logging.Formatter(fmt=DefaultConfig.LOG_FORMAT)
    sh.setFormatter(log_formatter)
    log_handlers.append(sh)

    logging.basicConfig(
        level=DefaultConfig.LOG_LEVEL,
        datefmt=DefaultConfig.LOG_DATEFORMAT,
        handlers=log_handlers,
        force=True,
    )
    log_tz = DefaultConfig.LOG_TZ

    # 在日志中使用指定的时区格式化时间戳 按照自己设定的时区显示时间 方便配置不同时区的日志
    if log_tz:
        from datetime import datetime

        import pytz

        timezone = pytz.timezone(log_tz)

        def time_converter(seconds):
            return datetime.utcfromtimestamp(seconds).astimezone(timezone).timetuple()

        for handler in logging.root.handlers:
            handler.formatter.converter = time_converter


"""another log config but not try
import logging
from logging.handlers import RotatingFileHandler

from flask import has_request_context, request


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


formatters = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
)

flask_file_handle = RotatingFileHandler('static/logg.log', 'a', 300 * 1024 * 1024, 10)
flask_file_handle.setFormatter(formatters)

formatter = logging.Formatter('[%(asctime)s]%(filename)s-%(funcName)s-%(lineno)d\n-%(message)s')

file_handle = RotatingFileHandler('static/lo.log', 'a', 300 * 1024 * 1024, 10)
file_handle.setFormatter(formatter)

# 如果把pass改成__name__会打印两次日志
logged = logging.getLogger('pass')
logged.addHandler(file_handle)
logged.setLevel("DEBUG")
"""
