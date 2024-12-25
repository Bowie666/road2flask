from flask import Blueprint
from flask_restful import Resource, Api, reqparse, inputs

# TODO 有什么好的用法在补充吧
basic_bp = Blueprint("basic", __name__)
basic_api = Api(basic_bp)


class HelloWorldResource(Resource):
    def get(self):
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


basic_api.add_resource(HelloWorldResource, '/')
basic_api.add_resource(ParaResource, '/para')
