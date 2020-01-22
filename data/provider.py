import json
import pathlib

data_dir = pathlib.Path(__file__).parent.absolute()

def get_goals():
    # In good way I'll create a module-level variable to read file only once
    # But this approach gives a flexibility on development
    # And optimization is postponed on purpose
    with open(f'{data_dir}/goals.json') as file:
        return json.loads(file.read())

def get_teachers(goal=None):
    with open(f'{data_dir}/teachers.json') as file:
        teachers = json.loads(file.read())

    if goal:
        teachers = filter(lambda teacher: goal in teacher['goals'], teachers)

    return teachers

def save_teachers(teachers):
    with open(f'{data_dir}/teachers.json', 'w') as file:
        file.write(json.dumps(teachers))

def get_teacher(id):
    teachers = get_teachers()

    for teacher in teachers:
        if teacher['id'] == id:
            return teacher

def save_lesson_request(data):
    print('data', data)
    try:
        with open(f'{data_dir}/requests.json') as file:
            list = json.loads(file.read())
    except OSError:
        list = []
    except json.decoder.JSONDecodeError:
        list = []

    list.append(data)

    with open(f'{data_dir}/requests.json', 'w') as file:
        file.write(json.dumps(list))

def save_lesson_booking(booking_request):
    save_lesson_request(booking_request)

    teachers = get_teachers()
    for teacher in teachers:
        if teacher['id'] == booking_request['teacher_id']:
            teacher['free'][booking_request['day']][booking_request['time']] = False

    save_teachers(teachers)