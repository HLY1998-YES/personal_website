import os
from flask import Flask

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.abspath("templates"),  # 确保模板目录正确
        static_folder=os.path.abspath("static")  # 确保静态文件目录正确
    )

    from app.routes import setup_routes
    setup_routes(app)

    return app
