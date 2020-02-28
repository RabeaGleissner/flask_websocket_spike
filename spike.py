from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-secret'
socketio = SocketIO(app)

@app.route('/')
def home():
    return 'Hello World'

@socketio.on('connect', namespace='/test')
def test_connect():
    print('socketio.on connect')
    emit('my_response', {'data': 'Connected (lifecycle method)'})

@socketio.on('custom_connection_event', namespace='/test')
def custom_connection_message(message):
    print('custom_connection_event with message:', message)
    emit('my_response', {'data': 'You told me you are connected!'})

@socketio.on('ping_event', namespace='/test')
def ping(message):
    emit('my_response', {'data': 'Thanks for the ping'})

@socketio.on('disconnect_request', namespace='/test')
def disconnect_request(message):
    print('received disconnect_request', message)
    disconnect()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected (lifecycle method)')

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
