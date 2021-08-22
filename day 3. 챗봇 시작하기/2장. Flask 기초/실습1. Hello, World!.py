# pip install flask
from flask import Flask

app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
# 아래 코드는 수정하지 마세요.
app.run('0.0.0.0', port=8888, threaded=True)