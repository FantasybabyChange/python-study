# -*- coding:utf-8 -*-   # 这行声明python源文件编码，编码信息会被解释器用于解析源文件
from flask import Flask, request, Response, jsonify
import os

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    if request.is_json:
        script_str = str(request.get_json())
    else:
        script_str = str(request.get_data(), encoding="utf8")
    if script_str is None:
        return 'empty data script send failed'  # 啥都没有
    print(script_str)
    script_save_path = "/home/fantasybaby/script"
    print(script_str['error_code'])
    print(script_str['error_level'])
    file_full_path = script_save_path + '/script.txt'
    if not os.path.exists(script_save_path):
        os.makedirs(script_save_path)
        print('create dir %s success' % script_save_path)
    with open(file_full_path, 'w') as script_file:
        script_file.write(script_str)

    return ' send success!'  # 返回保存成功的信息


@app.route('/send_json', methods=['POST'])
def send_json():
    if request.is_json:
        script_str = dict(request.get_json())
    else:
        script_str = str(request.get_data(), encoding="utf8")
    if script_str is None:
        return 'empty data script send failed'  # 啥都没有
    print(script_str)
    print(script_str.get('error_code'))
    print(script_str.get('error_level'))
    return ' send success!'  # 返回保存成功的信息


print(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
    # 会调用werkzeug.serving.run_simple进入轮询
    # 默认使用单进程单线程的werkzeug.serving.BaseWSGIServer处理请求
    # 实际上还是使用BaseHTTPServer.HTTPServer，通过select.select做0.5秒的"while True"事件轮询。
    # app.run()的启动方式只适合调试
