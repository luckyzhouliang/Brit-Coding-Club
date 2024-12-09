import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

prefix = 'sqlite:///'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE','data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY','dev')

db = SQLAlchemy(app)

login_manager = LoginManager(app)  # 实例化扩展类
login_manager.login_view = 'login'

from watchlist import views, errors, commands
from watchlist.models import User


@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象


# 注入上下文
@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)
