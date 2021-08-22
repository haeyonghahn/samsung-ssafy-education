from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# int형 변수를 받는 함수를 작성하세요. 
@app.route('/rabbit/<int:rabbit_num>')
def hell_rabbit(rabbit_num):
    return 'rabbit_num^2 = %d!' %(rabbit_num*rabbit_num)

# 아래 코드는 수정하지 마세요.
app.run('0.0.0.0', port=8888, threaded=True)
