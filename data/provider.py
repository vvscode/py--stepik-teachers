import json
import pathlib

data_dir = pathlib.Path(__file__).parent.absolute()

def get_goals():
    with open(f'{data_dir}/goals.json') as file:
        return json.loads(file.read())

def get_teachers(goal=None):
    with open(f'{data_dir}/teachers.json') as file:
        teachers = json.loads(file.read())

    if goal:
        teachers = filter(lambda teacher: goal in teacher['goals'], teachers)

    return teachers

def get_teacher(id):
    teachers = get_teachers()

    for teacher in teachers:
        if teacher['id'] == id:
            return teacher