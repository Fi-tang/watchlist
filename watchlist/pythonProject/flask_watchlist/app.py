'''
为了模拟页面渲染，我们需要先创建一些虚拟数据，用来填充页面内容:
'''
name = 'Fi-tang'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

'''
渲染主页模板
使用 render_template() 函数可以把模板渲染出来，必须传入的参数为模板名
(相对于 templates 根目录的文件路径), 这里即 'index.html'。
为了让模板正确渲染，我们还要把模板内部使用的变量通过关键字参数传入这个函数
'''
# 数据库配置
import os
import sys

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # 导入扩展类

WIN = sys.platform.startswith('win')
if WIN: # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  #  否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app) # 初始化扩展，传入程序实例 app

'''
目前我们有两类数据要保存: 用户信息和电影条目信息。
分别创建了两个模型类来表示这两张表:
1. 模型类要声明继承 db.Model。
2. 每个类属性(字段) 要实例化 db.Column, 传入的参数为字段的类型。
3. primary_key 设置当前字段是否为主键。
'''
class User(db.Model): # 表名将会是 user(自动生成，小写处理)
    id = db.Column(db.Integer, primary_key=True) # 主键
    name = db.Column(db.String(20)) # 名字

class Movie(db.Model): # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True) # 主键
    title = db.Column(db.String(60)) # 电影标题
    year = db.Column(db.String(4)) # 电影年份

'''
flask shell 激活了程序上下文，包含一些特殊变量，对于某些操作是必须的
可以编写自定义命令来自动执行创建数据库表操作:
--drop 作为命令行选项，用户可以通过 --drop (或 -d) 启用该选项，
is_Flag=True 表示这个选项不需要接参数值，它的存在就是一种标志。
initdb(drop) 是实际的命令函数，drop 参数会根据用户在命令行中是否使用 --drop 选项而被设置为 True 或 False。
'''
import click

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    '''Initialize the databse.'''
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.route('/')
def index():
    return render_template('index.html', name = name, movies= movies)