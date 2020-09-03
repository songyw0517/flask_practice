# flask & mysql connect

## 확인하고자 하는 것
> HTML에서 DB에 접근하여 insert, update, delete, select 등의 기능을 수행함 <br>
> add) BluePrint

# Blue_Print
Flask는 application component를 만들거나, applicaion 안팎으로 공통적인 패턴을 지원하는 목적으로 블루프린트라는 컨셉을 사용한다.

블루프린트는 큰 application을 단순화시키는 역할을 하고, Flask extension(확장 프로그램, 라이브러리 등) 등록을 위한 중심 수단으로도 쓰인다.

플라스크는 django와 달리 url들을 파일 단위에서 따로 관리하지 않고, controller의 endpoint 함수에 데코레이터를 붙여서 관리한다.

라우트함수(@app.route로 매핑되는 함수)들은 기능이 필요할때마다 계속 추가되어야 하기 때문에, create_app 함수내에 함수가 많을 경우 번거로워질 수 있다.

이런 상황에서 블루프린트(Blueprint)를 이용하면 라우트 함수들을 보다 구조적으로 관리할 수 있게 된다. 블루프린트에 대해서 자세히 알아보도록 하자.

## 파일 구조
<pre>
- /FLASK_DB_CONNECT_HTML
    - /app
        - /DB
        - /static
        - /templates
            - index.html
        - /view
            - index.py
        app.py
</pre>
파일 구조를 이렇게 한 것은 app.py에서 각각의 blueprint를 관리를 하기 위함이다.

view안의 파일은 각각의 html에서의 기능을 담은 파일을 의미한다.

index.py는 index.html에 있는 기능을 포함한 것이다.

이런 파일 구조라면 여러개의 html을 관리하는데 있어서 매우 편해질 것이다.

## Code Review
1. app/templates/index.html 은 일반적인 html문서이다.
2. app/view/index.py는 index.html의 기능을 명세한다.
3. app/app.py 는 BluePrint를 가져와 기능들을 관리한다.
<br>

### [app/view/index.py]
``` python 

from flask import Blueprint, render_template

BP = Blueprint('index', __name__, url_prefix='/') # Blueprint 객체를 생성한다. 
# url_prefix 는 index.py 파일의 모든 url의 앞에 붙는 것을 의미한다.

@BP.route('/')
def index():
    return render_template('index.html')
```
> view의 파일에서는 Blueprint 객체를 생성하고 메소드를 생성한다. 
<br>

### [app/app.py]
``` python
from flask import Flask, request, render_template
from DB import init_DB as db
from view import index # view 패키지에서 index 모듈을 가져온다.

app = Flask(__name__) # 앱 생성

app.register_blueprint(index.BP) # index의 BP를 blueprint에 등록한다.

if __name__== '__main__':
    app.run(debug=True)
```
> app.py 에서는 view 패키지 및 다른 패키지들에 대해 Blueprint 객체를 등록하고 관리해준다. 관리하는 것은 아마도 메소드를 만들어서 관리할 것 같다!