from flask import Flask

'''
!!!模型类被使用才能迁移成功!!!

pip install Flask-Migrate

flask db init               初始化迁移环境，只需运行一次
flask db migrate -m "msg"	生成迁移文件，msg 是对迁移内容的描述
flask db upgrade	        应用迁移，将数据库更新到最新版本
flask db downgrade	        回退迁移，将数据库恢复到上一版本
flask db current	        查看当前数据库迁移版本
flask db history	        查看迁移历史
flask db show [revision]	查看特定迁移版本的详细信息

# 在删除字段或表时，确保数据备份完好，或确认不会影响现有功能。
'''
def init_app(app: Flask):
    import flask_migrate

    from extensions.ext_db import db

    flask_migrate.Migrate(app, db)
