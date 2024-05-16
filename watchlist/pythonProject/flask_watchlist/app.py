from flask import Flask
'''
从 flask 包导入 Flask 类，通过实例化这个类，创建一个程序对象 app
'''

app = Flask(__name__)

'''
注册一个处理函数，函数是处理某个请求的处理函数，Flask 官方称为视图函数(view function),
,理解为"请求处理函数"
所谓的"注册”，就是给这个函数戴上一个装饰器帽子。我们使用 app.route() 装饰器来为这个函数绑定对应的 URL,
当用户在浏览器访问这个URL的时候，就会触发这个函数，获取返回值，并把返回值显示到浏览器窗口: 
> Web程序看作是一堆这样的视图函数的集合: 编写不同的函数处理对应 URL 的请求

填入 app.route() 装饰器的第一个参数是 URL 规则字符串，这里的 / 指的是根地址。
我们只需要写出相对地址，主机地址、端口号等都不需要写出。
这里的 / 对应的是主机名后面的路径部分，完整 URL 就是 http://localhost:5000/
如果定义的 URL 规则是 /hello，完整 URL 就是 http://localhost:5000/hello
'''
@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'