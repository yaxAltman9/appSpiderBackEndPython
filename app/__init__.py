from flask import Flask
from app.controllers import job_bp
from app.config import Config
from flask_mysqldb import MySQL
import logging

app = Flask(__name__)
app.config.from_object(Config)

# 设置日志
logging.basicConfig(level=logging.INFO)

# 初始化 MySQL
mysql = MySQL(app)

app.register_blueprint(job_bp)

def create_app():
    return app
