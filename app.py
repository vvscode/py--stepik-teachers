from flask import Flask, render_template, abort
from data import provider

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.j2',
                           goals=provider.get_goals(),
                           teachers=provider.get_teachers()
                           )


@app.route('/goals/<goal>/')
def goals(goal):
    return render_template('goal.j2',
                           title=provider.get_goals().get(goal, 'Uknown goal'),
                           teachers=provider.get_teachers(goal=goal)
                           )


@app.route('/profiles/<int:id>/')
def profile(id):
    teacher = provider.get_teacher(id)

    if not teacher:
        abort(404)

    return render_template('profile.j2', teacher=teacher)


@app.route('/search')
def search():
    return 'Search'


@app.route('/request/')
def request():
    return render_template('request.j2')


@app.route('/booking/<int:id>/')
def booking(id):
    teacher = provider.get_teacher(id)

    if not teacher:
        abort(404)

    return render_template('booking.j2', teacher=teacher)


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            "404.j2", title="404"
        ),
        404,
    )
