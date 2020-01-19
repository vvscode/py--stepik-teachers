from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.j2')


@app.route('/goals/')
def goals():
    return render_template('goal.j2')


@app.route('/profiles/<id>/')
def profile():
    return render_template('profile.j2')


@app.route('/search')
def search():
    return 'Search'


@app.route('/request/')
def request():
    return 'request'


@app.route('/booking/<id>/')
def booking():
    return render_template('booking.j2')


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            "404.j2", title="404"
        ),
        404,
    )
