from flask import Flask, render_template, abort, request, redirect, url_for
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
        return abort(404)

    return render_template('profile.j2', teacher=teacher)


@app.route('/search')
def search():
    return 'Search'


@app.route('/request/', methods=['GET', 'POST'])
def request_lesson():
    if request.method == 'POST':
        lesson_request = {
            'goal': request.form['goal'],
            'time': request.form['time'],
            'name': request.form['name'],
            'phone': request.form['phone'],
        }
        provider.save_lesson_request(lesson_request)
        return render_template('request_done.j2', request=lesson_request)

    return render_template('request.j2')


@app.route('/booking/<int:id>/<day>/<time>', methods=['GET', 'POST'])
def booking(id, day, time):
    teacher = provider.get_teacher(id)

    if not teacher:
        return abort(404)

    if day not in teacher['free']:
        # incorrect day input
        return abort(404)

    if time not in teacher['free'][day]:
        # incorrect time input
        return abort(404)

    if not teacher['free'][day][time]:
        # time is booked
        return abort(404)

    if request.method == 'POST':
        booking_request = {
            'teacher_id': id,
            'day': day,
            'time': time,
            'name': request.form['name'],
            'phone': request.form['phone']
        }
        provider.save_lesson_booking(booking_request)

        return render_template('booking_done.j2', booking_request=booking_request)

    return render_template('booking.j2',
                           teacher=teacher,
                           day=day,
                           time=time,
                           id=id
                           )


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            "404.j2", title="404"
        ),
        404,
    )
