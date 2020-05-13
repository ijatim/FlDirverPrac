from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghijkl1234#'
sio = SocketIO(app)


@app.route('/')
def session():
    return render_template('session.html')


def receive_massage(methods=['GET', 'POST']):
    print('Successful')


@sio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('revieved my event: ' + str(json))
    sio.emit('my response', json, callback=receive_massage)

if __name__ == '__main__':
    sio.run(app, debug=True)