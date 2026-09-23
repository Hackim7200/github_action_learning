# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  
    return 'Hello, World!'

@app.route('/count')
def count():
     
    return 'Count page!'

@app.route('/somethingelse')
def something_else():
     
    return 'Something else page!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)