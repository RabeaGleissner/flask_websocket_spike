from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

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

