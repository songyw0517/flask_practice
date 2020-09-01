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