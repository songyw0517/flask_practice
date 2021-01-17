from flask import Blueprint, render_template, request, jsonify
from DB import db
BP = Blueprint('login', __name__, url_prefix='/login_page')

@BP.route('/login_page')
def login_page():
    return render_template('login.html')


@BP.route('/login', methods=['POST', 'GET'])
def login():
    try:
        if request.method=='POST':
            print("로그인")
            scof_col = db.connect_db_return_scof_col() #db연결
            id = request.form['id']
            pw = request.form['pw']
            print("로그인 id=", id, 'pw=', pw)
            return render_template('login.html')
        elif request.method=='GET':
            print("GET")
    except:
        print('예외')
@BP.route('/register')
def register():
    return render_template('regiter.html')