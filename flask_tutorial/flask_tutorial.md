# Flaskr 소개하기
> 우리는 우리의 블로깅 어플리케이션을 flaskr 이라고 부를 것이다. 웬지 덜 웹 2.0스러운 이름을 선택해야할 것 같은 느낌에서 자유로워 진것 같다. 기본적으로 우리는 flaskr을 통해서 다음 사항들을 하기를 원한다:

1. 사용자가 지정한 자격증명 설정을 이용하여 로그인/로그아웃을 할 수 있게 한다.
사용자는 단한명만 지원한다.
2. 사용자가 로그인하면 사용자는 제목과 내용을 몇몇 HTML과 텍스트로만 입력할 수 있다.
우리는 사용자를 신뢰하기 때문에 HTML에 대한 위험성 검증은 하지 않는다.
3. flaskr 페이지에서는 지금까지 등록된 모든 항목들을 시간의 역순으로 상단에 보여준다 최근것을 제일 위로)`(최근것을 제일 위로) 로그인한 사용자는 새로 글을 추가 할 수 있다.

> 이정도 규모의 어플리케이션에서 사용하기에는 SQLite3도 충분한 선택이다. <br>
그러나 더 큰 규모의 어플리케이션을 위해서는 더 현명한 방법으로 데이타베이스 연결을 핸들링하고 다른 RDBMS를 사용이 가능한 SQLAlchemy 를 사용하는 것이 맞다. <br>
> 만약 여러분의 데이타가 NoSQL에 더 적합하다면 인기있는 NoSQL 데이타베이스 중 하나를 고려하기를 원할 수도 있다.

아래는 최종 완성된 어플리케이션의 스크린샷이다.:
![ex_screen](./img_for_git/ex_screen.png)

# 폴더 생성
<pre>
/flaskr
    /static
    /templates
</pre>
> flaskr폴더는 python 패키지가 아니다. 단지 우리의 파일들을 저장할 장소이다. 우리는 이 폴더 안에 데이터베이스 스키마 뿐만 아니라 주요 모듈들을 넣을 수 있다.<br>
> static폴더 내 파일들은 HTTP를 통해 어플리케이션 사용자들이 이용할 수 있다. (css, js등의 파일들이 저장된다.)

# 데이터베이스 스키마 생성
먼저 우리는 데이터베이스 스키마를 생성해야 한다. 우리의 어플리케이션을 위해서는 단지 하나의 테이블만 필요하며 사용이 매우 쉬운 SQLite를 지원하기를 원한다. 다음의 내용을 schema.sql 이라는 이름의 파일로 방금 생성한 flaskr 폴더에 저장한다.
``` sql
drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);
```

# 어플리케이션 코드
flaskr.py 파일 생성.
``` python
# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__) # object는 인자로 주어진 객체를 읽어오기 위함이다.
#.from_object(__name__) 대신 app.config.from_envvar('FLASKR_SETTINGS', silent=True) 를 사용할 수 있다.

# connect DB
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()
```

# 데이터베이스 생성
> 데이터베이스를 초기화 하는 함수를 추가하기 위해서 contextlib의 contextlib.closing()함수가 필요하다. (__future__를 먼저 import해야한다.)
```python
from __future__ import with_statement
from contextlib import closing
```
``` python
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
```
이 두 코드를 flaskr.py에 추가한다.