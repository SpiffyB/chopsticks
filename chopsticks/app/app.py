from flask import Flask, redirect, url_for, request, render_template
from threading import Thread
from . import config


app = Flask(__name__)
app.config.from_object(config.Config)

@app.route('/')
def hello_world_route():
    """Print 'Hello, world!' as the response body."""
    return "Hello World"

@app.route('/index')
def index():
    return render_template('index.html', title='Home', user="test_user")


class flask_app(Thread):
    global app

    def run(self):
        app.run(host="localhost", port="6969", debug=True, use_reloader=False)

    def hello_world(self):
        """Print 'Hello, world!' as the response body."""
        return hello_world_route()

    def messageReceived(methods=['GET', 'POST']):
        print('message was received!!!')

