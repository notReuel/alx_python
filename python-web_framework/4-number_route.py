"""FLASK initialized"""
from flask import Flask

app = Flask(__name__)

"""
    Route the app
"""
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'    

@app.route('/c/<text>', strict_slashes=False)
def CisFun(text):
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythonIsFun(text='is cool'):
    formatted_text = text.replace('_', ' ')
    return 'Python {}'.format(formatted_text)

@app.route('/number/<n>', strict_slashes=False)
def num(n):
    if n is isinstance(n, int):
        return n
    else: 
        return "n is anumber                                                                           "


if __name__ == '__main__':
    # port and host to run flask app
    app.run(host='0.0.0.0', port=5000)

