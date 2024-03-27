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
    return 'C {}'.format(text)


if __name__ == '__main__':
    # port and host to run flask app
    app.run(host='0.0.0.0', port=5000)

