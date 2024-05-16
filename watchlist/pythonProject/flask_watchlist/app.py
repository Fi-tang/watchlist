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

'''
可以自由传入 app.route 装饰器中的 URL 规则字符串，但是需要注意以斜线 / 作为开头。
一个视图函数也可以绑定多个URL，这通过附加多个装饰器实现
'''
@app.route('/index')
@app.route('/')
@app.route('/home')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

'''
前面，之所以把传入 app.route 的装饰器的参数称为 URL 规则，是因为我们也可以在 URL 里定义变量部分。
下面这个视图函数会处理所有类似 /user/<name> 的请求
不论你访问 http://localhost:5000/user/greyli, 还是 http://localhost:5000/user/peter 或者是
http://localhost:5000/user/甲 都会触发这个函数。
'''
@app.route('/user/<name>')
def user_page(name):
    return 'User Page'
'''
从视图函数中获取这个变量值:
用户输入的数据会包含恶意代码，所以不能直接作为响应返回，需要使用 MarkupSafe(Flask 的依赖之一)
提供的 escape() 函数对 name 变量进行转义处理，
比如把 < 转换成 &lt;。这样在返回响应时浏览器就不会把它们当作代码执行
'''
from markupsafe import escape
@app.route('/host/<name>')
def host_page(name):
    return f'Host: {escape(name)}'

'''
修改视图函数名?
最后一个可以修改的部分就是视图函数的名称了。视图函数的名字是自由定义的，和 URL 规则无关.
和定义其他函数或变量一样，只需要让它表示出所要处理页面的含义即可。

除此之外，它还有一个重要的作用：作为代表某个路由的端点(endpoint),同时用来生成视图函数对应的 URL。
对于程序内的 URL, 为了避免手写，Flask 提供了一个 url_for 函数来生成 URL,它接受的第一个参数就是端点值，默认为视图函数的名称
'''
from flask import url_for
@app.route('/test')
def test_url_for():
    # 下面是一些调用示例,(访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL);
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL, 将会输出: /
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出: /user/greyli
    print(url_for('user_page', name='peter'))  # 输出: /user/peter
    print(url_for('test_url_for')) # 输出: /test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面.
    print(url_for('test_url_for', num=2)) # 输出: /test?num=2
    return 'Test page'