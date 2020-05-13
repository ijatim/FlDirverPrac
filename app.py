from flask import Flask
from flask_socketio import SocketIO
import sqlite3

app = Flask(__name__)
app.config['SECRET KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
    #socketio.run(app)
