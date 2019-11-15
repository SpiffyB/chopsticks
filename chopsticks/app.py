from flask import Flask, redirect, url_for, request, render_template
from flask_socketio import SocketIO
import threading


app = Flask(__name__)
socketio = SocketIO(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio.run(app, host = "localhost", port = 3000, debug = True)

@app.route('/')
def hello_world(self):
    """Print 'Hello, world!' as the response body."""
    return "Hello World"

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

### Receiving WebSocket Messages ###
@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
