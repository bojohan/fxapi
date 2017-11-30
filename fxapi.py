from flask import Flask

app = Flask(__name__)


# this is a decorator
@app.route('/')
# this is a function
def hello_world():
    return 'Hello World!'


@app.route('/hello/<name>')
def hello_again(name):
    return 'Hello ' + name

if __name__ == '__main__':
    app.run(port= 5005,debug=True)
