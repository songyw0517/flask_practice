from flask import Flask, request, render_template
from DB import init_DB as db
from view import index
app = Flask(__name__)

app.register_blueprint(index.BP)

@app.before_request
def before_request():
    db.get_db()

@app.teardown_request
def teardown_request(exception):
    db.close_db()

def init_app():
    #DB 초기화
    db.init_db()

if __name__== '__main__':
    init_app()
    app.run(debug=True)