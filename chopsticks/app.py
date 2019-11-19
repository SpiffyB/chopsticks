from flask import Flask, redirect, url_for, request, render_template
from threading import Thread

class flask_app(Thread):
    app = Flask(__name__)

    def __init__(self):
        Thread.__init__(self)
        self.app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
        self.app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

    def run(self):

        self.app.run(host="localhost", port="6969", debug=True, use_reloader=False)

    @app.route('/')
    def hello_world(self):
        """Print 'Hello, world!' as the response body."""
        return "Hello World"

    def messageReceived(methods=['GET', 'POST']):
        print('message was received!!!')

