from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

@app.route('/goals/')
def goals():
    return '/goals/'

@app.route('/profiles/<id>/')
def profile():
    return 'Profile'

@app.route('/search')
def search():
    return 'Search'

@app.route('/request/')
def request():
    return 'request'

@app.route('/booking/<id>/')
def booking():
    return 'booking'


if __name__ == '__main__':
    app.run()
