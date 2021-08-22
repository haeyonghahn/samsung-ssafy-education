from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 변수 값을 받는 함수를 작성하세요.
@app.route('/rabbit/<rabbitname>')
def hello_rabbit(rabbitname) :
    return 'Hello, ' + rabbitname + '!'

# 아래 코드는 수정하지 마세요.
app.run('0.0.0.0', port=8888, threaded=True)