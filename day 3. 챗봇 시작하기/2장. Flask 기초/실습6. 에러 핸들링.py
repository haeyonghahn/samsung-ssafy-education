from flask import Flask

app = Flask (__name__)


@app.errorhandler(404) # 에류 종류 표시
def page_not_found(error):
    return "<h1>404 Error - Page Not Found</h1>", 404

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
# 아래 코드는 수정하지 마세요.
app.run('0.0.0.0', port=8888, threaded=True)