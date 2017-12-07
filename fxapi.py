from flask import Flask, jsonify
from fxlib import fxdata



app = Flask(__name__)


# this is a decorator
@app.route('/')
# this is a function
def hello_world():
    return 'Hello World!'


@app.route('/hello/<name>')
def hello_again(name):
    return 'Hello ' + name

@app.route('/<currency>')
def get_currency(currency):
    return jsonify(fxdata())



if __name__ == '__main__':
    app.run(port= 5005,debug=True)
