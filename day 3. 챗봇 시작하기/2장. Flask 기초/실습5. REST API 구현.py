from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {'animal':'rabbit', 'fruit':'apple'}
    return jsonify(data)

@app.route('/elice_info')
def hello_rabbit():
    data = {'rabbit':'white', 'character':'elice'}
    return jsonify(data)
    
# 아래 코드는 수정하지 마세요.
app.run('0.0.0.0', port=8888, threaded=True)
