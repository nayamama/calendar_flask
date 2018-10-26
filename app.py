import os
from flask import Flask
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<name>')
def hello_name(name):
    return "hello {}".format(name)


if __name__ == '__main__':
    app.run()
