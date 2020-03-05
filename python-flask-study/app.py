# -*- coding:utf-8 -*-   # 这行声明python源文件编码，编码信息会被解释器用于解析源文件
from flask import Flask,request,Response,jsonify

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    print(request.get_json())
    print(request.args["a"])

    return "hello world"


print (__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
    # 会调用werkzeug.serving.run_simple进入轮询
    # 默认使用单进程单线程的werkzeug.serving.BaseWSGIServer处理请求
    # 实际上还是使用BaseHTTPServer.HTTPServer，通过select.select做0.5秒的"while True"事件轮询。
    # app.run()的启动方式只适合调试
