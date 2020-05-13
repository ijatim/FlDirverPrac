from flask import Flask
from flask_socketio import SocketIO
import sqlite3

app = Flask(__name__)
app.config['SECRET KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    socketio.run()
