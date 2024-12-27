from flask import Blueprint, current_app
from flask_restful import Resource, Api, reqparse, inputs

from tasks.time_task import long_task
from celery.result import AsyncResult

# TODO 有什么好的用法在补充吧
basic_bp = Blueprint("basic", __name__)
basic_api = Api(basic_bp)


class HelloWorldResource(Resource):
    def get(self):
        redis_client = current_app.extensions["redis"]
        # redis报错还是会正确返回
        redis_client.set('key', '1')
        print('write redis success')

        return {'hello': 'world'}

    def post(self):
        return {'msg': 'post hello world'}


class ParaResource(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        parser = reqparse.RequestParser()  # 这段代码放哪无所谓 放类外面也行
        parser.add_argument(
            'rate', 

            # type=int  type=float  type=str  type=list     
            type=str,
            # type=inputs.regex(r'^\d{2}&')  # 可用正则表达式检验参数

            help='Rate cannot be converted',   # 参数检验错误时返回的错误描述信息

            # location='args',  # 参数存放的位置
            location=['args', 'cookies', 'headers', 'json', 'files', 'form'],  # 参数存放的位置 可指定多个

            action='store',  # 保留出现的第一个， 默认
            # action='append'   # 以列表追加保存所有同名参数的值

            )
        parser.add_argument('name')
        args = parser.parse_args()

        return {
            'rate': args['rate'], 
            'name': args.name, 
            'msg': 'post hello world'
        }


class TiemTaskAPI(Resource):
    def put(self, task_id):
        tid = [task_id]
        task = long_task.apply_async()  # 启动异步任务
        return { 'task_id': task.id }

    def get(self, task_id):
        # task = long_task.AsyncResult(task_id)  # 获取任务状态
        task = AsyncResult(task_id)  # 获取任务状态
        return {
            'task_id': task.id,
            'status': task.status,
            'result': task.result,
            "ready": task.ready(),
            "successful": task.successful(),
            "value": task.result if task.ready() else None,
        }


basic_api.add_resource(HelloWorldResource, '/')
basic_api.add_resource(ParaResource, '/para')
basic_api.add_resource(TiemTaskAPI, '/task/<task_id>')
