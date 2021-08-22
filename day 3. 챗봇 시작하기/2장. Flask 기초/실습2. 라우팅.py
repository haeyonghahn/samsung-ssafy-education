from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
# 경로가 rabbit인 경우 'Hello, Rabbit!'을 띄우는 코드를 작성하세요. 
@app.route('/rabbit')
def hello_rabbit():
    return 'Hello, Rabbit!'
# 아래 코드는 수정하지 마세요.
app.run('0.0.0.0', port=8888, threaded=True)