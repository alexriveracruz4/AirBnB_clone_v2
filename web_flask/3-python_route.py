#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb/')
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    """ display 'C ' followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def pythontext(text='is cool'):
    """display 'Python ', followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
