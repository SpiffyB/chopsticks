from flask import Flask, redirect, url_for, request, render_template, flash
from threading import Thread
from . import config, forms


app = Flask(__name__)
app.config.from_object(config.Config)

@app.route('/')
def hello_world_route():
    """Print 'Hello, world!' as the response body."""
    return "Hello World"

@app.route('/index', methods=['GET','POST'])
def index():
    form = forms.GameForm()
    if form.validate_on_submit():
        flash('button pressed {}'.format(form.btn_player1_hand1.data))
    return render_template('index.html', title='Home', user="test_user", form=form)


class flask_app(Thread):
    global app

    def run(self):
        app.run(host="localhost", port="6969", debug=True, use_reloader=False)

    def hello_world(self):
        """Print 'Hello, world!' as the response body."""
        return hello_world_route()

    def messageReceived(methods=['GET', 'POST']):
        print('message was received!!!')

