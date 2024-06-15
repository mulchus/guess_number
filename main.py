from flask import Flask, request, session
from environs import Env

env = Env()
env.read_env()

app = Flask(__name__)
app.secret_key = env("SECRET_KEY")


@app.route('/')
def start():
    session.clear()
    return 'Start ok. First set max_number and hidden_number'


@app.route('/set_numbers/')
def set_numbers():
    session['max_number'] = int(request.args['max_number'])
    session['hidden_number'] = int(request.args['hidden_number'])
    if session['hidden_number'] > session['max_number']:
        return 'hidden_number must be less or equal than max_number'
    elif session['hidden_number'] < 0:
        return 'hidden_number must be greater or equal than 0'
    return {'numbers': session}


@app.route('/guess_number/<int:selected_number>')
def guess_number(selected_number):
    if 'hidden_number' not in session:
        return 'First set max_number and hidden_number'
    result = -1 if selected_number > session['hidden_number'] else 1 if selected_number < session[
        'hidden_number'] else 0
    if not result:
        session['guess_number'] = selected_number
        return {'result': result, 'guess_number': session['guess_number']}
    return {'result': result}
