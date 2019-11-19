from flask import Flask, redirect, url_for, request, render_template
from threading import Thread

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

@app.route('/')
def hello_world_route():
    """Print 'Hello, world!' as the response body."""
    return "Hello World"




class flask_app(Thread):
    global app

    def run(self):
        app.run(host="localhost", port="6969", debug=True, use_reloader=False)

    def hello_world(self):
        """Print 'Hello, world!' as the response body."""
        return hello_world_route()

    def messageReceived(methods=['GET', 'POST']):
        print('message was received!!!')

