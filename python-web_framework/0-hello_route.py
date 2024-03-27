from flask import Flask

app = Flask(__name__)

app.route('/', strict_slashes=False)
def hello_hello():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # port and host to run flask app
    app.run(host='0.0.0.0', port=5000)
    