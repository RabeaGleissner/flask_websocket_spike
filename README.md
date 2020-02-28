# Flask with React with Websockets

How to run this locally:

## 1) Set up the Flask app

`virtualenv venv`

`pip install -r requirements.txt`

## 2) Set up the React part

#### You have to be in the `frontend` directory for this.

`npm install`

`npm run build`

This will bundle the JavaScript and place it in  the `static/` directory.

## 3) Now you can run the Flask app

`export FLASK_APP=spike.py`

`flask run`

If you want to use the web socket connection, you might have to run it with

`python3 spike.py`
