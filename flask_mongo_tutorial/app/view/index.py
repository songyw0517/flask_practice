from flask import Blueprint, render_template, request, jsonify
from DB import db
BP = Blueprint('main', __name__, url_prefix='/')

@BP.route('/')
def index():
    #scof_col = db.connect_db_return_scof_col()
    return render_template('index.html')

@BP.route('/insert', methods=['POST', 'GET'])
def insert():
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    try:
        if request.method == 'POST':
            scof_col = db.connect_db_return_scof_col() # db연결 // ++ 일단 기능하는것에 집중함, 코드 바꿔야 할 수도있음
            #temp = request.form['num']
            id = request.form['id']
            pw = request.form['pw']
            msg = "id = "+id+" pw = "+pw
            value = {"_id" : id, "pw" : pw}
            
            result = scof_col.insert_one(value) # db에 삽입
            print("삽입된 data = ", result)
            
            
            '''확인하는 부분'''
            read()
            doc_list=[]
            for i in scof_col.find():
                print(i)
                doc_list.append(i)
            return render_template('index.html', msg=msg, data_list=doc_list)
            
        elif request.method == 'GET':

            ## 넘겨받은 숫자 
            print('get으로 넘어옴')
        ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함
    except:
        print("중복? 또는 문법오류겠지")
        return render_template('index.html')

@BP.route('/read', methods=['POST','GET'])
def read():
    try:
        if request.method == 'POST':
            scof_col = db.connect_db_return_scof_col() # db연결 // ++ 일단 기능하는것에 집중함, 코드 바꿔야 할 수도있음
            doc_list=[]
            for i in scof_col.find():
                print(i)
                doc_list.append(i)
            return render_template('index.html', data_list=doc_list)
    
    except:
        print("예외처리")
        return render_template('index.html')

@BP.route('/update', methods=['POST','GET'])
def update():
    try:
        if request.method == 'POST':
            scof_col = db.connect_db_return_scof_col() # db연결 // ++ 일단 기능하는것에 집중함, 코드 바꿔야 할 수도있음
            id = request.form['id']
            ch_pw = request.form['ch_pw']
            result = scof_col.update({'_id':id}, {"$set":{'pw' :ch_pw}}, upsert=True, multi=False)
            print("변경된 데이터 : ", result)
            
            '''확인하는 부분'''
            doc_list=[]
            for i in scof_col.find():
                print(i)
                doc_list.append(i)
            
            return render_template('index.html', up_data=result, data_list=doc_list)
        elif request.method == 'GET':
            print("get")
            return render_template('index.html')
    except:
        print("예외")
        return render_template('index.html')

@BP.route('/delete', methods=['POST', 'GET'])
def delete():
    try:
        if request.method == 'POST':
            scof_col = db.connect_db_return_scof_col() # db연결 // ++ 일단 기능하는것에 집중함, 코드 바꿔야 할 수도있음
            id = request.form['id']
            result = scof_col.find_one_and_delete( {"_id" : id} )
            print("삭제된 데이터 : ", result)

            '''확인하는 부분'''
            doc_list=[]
            for i in scof_col.find():
                print(i)
                doc_list.append(i)

            return render_template('index.html', del_data=result, data_list=doc_list)
        elif request.method == 'GET':
            return render_template('index.html', del_data = "get")    

    except:
        print("예외처리")
        return render_template('index.html', del_data = "터짐")
