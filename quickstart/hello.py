from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Glasgow! My name is ' + __name__


