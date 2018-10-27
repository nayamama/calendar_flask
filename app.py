import os
from flask import Flask, render_template, request, jsonify
#from flask import Flask
import configparser

app = Flask(__name__, static_url_path='/static')
config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<name>')
def hello_name(name):
    return "hello {}".format(name)


if __name__ == '__main__':
    app.run()
