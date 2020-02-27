from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-secret'
socketio = SocketIO(app)

@app.route('/')
def home():
    return 'Hello World'

@socketio.on('my_event', namespace='/test')
def test_message(message):
    print('socketio.on my_event')
    emit('my_response', {'data': message['data']})

@socketio.on('my_broadcast_event', namespace='/test')
def test_message(message):
    print('socketio.on my_broadcast_event')
    emit('my_response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    print('socketio.on connect')
    send('my_response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

@app.route('/with-template/')
@app.route('/with-template/<name>')
def with_template(name=None):
    return render_template('test_template.html', name=name)

@app.route('/form-data', methods=['POST'])
def login():
    print('Request object:')
    print(request)
    print(request.form)
    print(request.form['name'])
    return 'Thanks!'

if __name__ == '__main__':
    socketio.run(app)
