from flask import Blueprint, render_template, request

BP = Blueprint('main', __name__, url_prefix='/')

@BP.route('/')
def index():
    return render_template('index.html')

@BP.route('/insert', methods=['POST', 'GET'])
def insert():
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        print('post로 넘어왔음 request = ')
        id = request.form['id']
        pw = request.form['pw']
        msg = "id = "+id+" pw = "+pw
        value = (id, pw)
        return render_template('index.html', msg=msg)
    elif request.method == 'GET':
        ## 넘겨받은 숫자 
        print('get으로 넘어옴')
    ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함