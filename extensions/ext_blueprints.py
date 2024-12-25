from flask import Flask

from configs import DefaultConfig


def init_app(app: Flask):
    # register blueprint routers
    from flask_cors import CORS

    from apps.services import services_bp
    from apps.basicUse import basic_bp


    CORS(
        services_bp,
        resources={r"/*": {"origins": DefaultConfig.WEB_API_CORS_ALLOW_ORIGINS}},  # 定义了允许哪些路径和来源进行跨域请求
        supports_credentials=True,  # 是否支持跨域请求时发送身份验证信息（如 Cookies 或 HTTP 认证）。
        allow_headers=["Content-Type", "Authorization", "X-App-Code"],  # X-App-Code 是自定义的
        methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
        # expose_headers=["X-Version", "X-Env"],  # 指定客户端可以访问的响应头 这些可能是自定义的
    )

    app.register_blueprint(services_bp)


    app.register_blueprint(basic_bp)
