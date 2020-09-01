# flask & mysql connect

## 확인하고자 하는 것
> 템플릿을 랜더링하는 것은 추후에 할 예정이다.<br>
> 우선 파이썬과 mysql을 연동하는 것을 목표로 한다.

## 파일 구조
<pre>
- /flask_db_connect
    - /app
    - /DB
    - /static
    - /templates
    config.py
    main.py
</pre>

# install
pymysql을 사용하므로
> pip install pymysql

명령어로 설치한다.

# database 생성 및 초기화
> 각자의 방법으로 데이터베이스를 생성한다.

> 나는 mysql workbench를 활용하여 생성하였다.
``` sql
/* root 계정으로 접속, scof 데이터베이스 생성, scof 계정 생성 */
/* MySQL Workbench에서 초기화면에서 +를 눌러 root connection을 만들어 접속한다. */
DROP DATABASE IF EXISTS  scof;
DROP USER IF EXISTS  scof@localhost;
create user scof@localhost identified WITH mysql_native_password  by 'root';
create database scof;
grant all privileges on scof.* to scof@localhost with grant option;
commit;

/* DB선택 */
USE scof;
/*test table 생성*/
CREATE TABLE test_login(
	num		INTEGER	PRIMARY	KEY NOT NULL AUTO_INCREMENT,
    ID		VARCHAR(20),
    PW		VARCHAR(20)
);
/*test data 생성*/
INSERT INTO test_login (ID, PW) VALUES ('scof', 'sejong');
```

# config.py_작성
> 이 파일에는 데이터베이스의 정보를 담는다. 
``` python
db = {
    'host'     : 'localhost',
    'user'     : 'root',
    'password' : '패스워드',
    'port'     : '포트 번호',
    'database' : '데이터베이스 이름'
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
DB_info = f"host='{db['host']}', user='{db['user']}', password='{db['password']}', db='{db['database']}', charset='utf8'"

# DB_URL은 사용하지 않을 예정이다.
```

# main.py_작성
> 드디어 main.py를 작성한다. 먼저 flask의 기초가 되는 뼈대를 작성하자.
```python
from flask import Flask
app = Flask(__name__)
if __name__== '__main__':
    app.run()
```
> 데이터베이스를 연동하기 위해서 필요한 기능은
1. 데이터베이스 초기화 -> init_db()
2. 데이터베이스 가져오기 -> get_db()
3. 데이터베이스 닫기 -> close_db()

이며, 이는 하나의 모듈에 담으면 좋을 것 같다!

# init_DB.py_작성
``` python
import pymysql
from flask import g
import config as cf

DB_IP = cf.db['host']
DB_User = cf.db['user']
DB_PW = cf.db['password']
DB_Database = cf.db['database']
#################
def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host=DB_IP, user=DB_User, password=DB_PW, db=DB_Database, charset='utf8')

def close_db():
    db = g.pop('db', None)
    if db is not None:
        if db.open:
            db.close()
#####################
def init_db():
    # MySQL Connection 연결
    db = pymysql.connect(host=DB_IP, user=DB_User, password=DB_PW, db=DB_Database, charset='utf8')
    print("DB 연결 시작")
    # Connection 으로부터 Cursor 생성
    curs = db.cursor()

    #SQL문 실행
    sql = 'SELECT * FROM test_login'
    curs.execute(sql)

    # 데이터 fetch ?
    rows = curs.fetchall()
    print(rows)
    db.close()
```
각각의 기능을 수행하는 메소드를 만들어 주었다. (아직 코드에 대한 이해는 부족하다.)

init_db() 메소드에서는 DB연결이 되었는지 확인하기 위하여 
> print("DB 연결시작")

으로 확인해주었으며, 데이터 fetch 부분에서 데이터베이스 데이터를 가져와 print(rows)로 출력해주었다.

# main.py_작성 마무리
```python
from flask import Flask, request # flask와 request를 사용
from DB import init_DB as db # DB폴더의 init_DB 모듈을 db라는 이름으로 사용할 것이다.

app = Flask(__name__)

@app.before_request # 매 HTTP 요청이 처리되기 전에 실행하는 데코레이터
def before_request(): # 계속해서 DB를 가져온다.
    db.get_db()

@app.teardown_request # 매 HTTP요청의 결과가 브라우저에 응답하고 나서 호출되는 데코레이터
def teardown_request(exception): # 응답하고 나서는 DB를 사용하지 않으므로 연결을 끊는다.
    db.close_db()

def init_app():
    #DB 초기화
    db.init_db()

if __name__== '__main__':
    init_app()
    app.run()
```

이제 main.py를 실행시키면 DB 연결 시작이라는 안내문과 함께 DB의 데이터를 가져오고, 서버?가 열리는 것을 확인할 수 있다.
