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
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', name = name, movies= movies)