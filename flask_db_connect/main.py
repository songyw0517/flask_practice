from flask import Flask, render_template, request
from DB import init_DB as db

app = Flask(__name__)

@app.before_request
def before_request():
    db.get_db()

@app.teardown_request
def teardown_request(exception):
    db.close_db()

@app.route('/')
def index():
    return render_template('index.html')

def init_app():
    #DB 초기화
    db.init_db()

if __name__== '__main__':
    init_app()
    app.run()