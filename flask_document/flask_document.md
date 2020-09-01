# flask_practice
flask_practice

# flask install

# flask document
>기본이 되는 코드
``` python
from flask import Flask # flask import
app = Flask(__name__) # Flask 객체를 생성한다.
'''
1. 인자로 들어가는 것은 응용 프로그램의 모듈 또는 패키지의 이름이다.
2. 단일 모듈을 사용하는 경우에는 ___name__을 사용해야 한다. 
이 코드에서 app을 실행시키면 __name__이 아닌 __main__이 들어가게 된다. 
즉 수행되는 모듈의 이름이 __main__이라고 생각하면 될 것 같다.
3. 자세한 내용은 찾아보자
'''
@app.route('/') # @은 데코를 의미한다. 인자의 값의 URL에 접속할 때 수행할 기능을 작성한다.
def hello_world():
    return 'Hello World'
if __name__ == '__main__':
    app.run()
```

실행 후 접속한 결과.

![flask_ex1](./img_for_git/flask_1.png)

------------------------------------------------------------------------
> 디버그 모드

만약 오류가 생긴다면 디버그 모드로 확인할 수 있다.
```python
if __name__ == '__main__':
    app.run(debug=True) # 이것을 적어주면 된다.
```
-----------------------------------------------------------

> 외부에서 접근 가능한 서버

위의 서버를 실행했다면, 그 서버는 네트워크상에 있는 다른 컴퓨터에서 접근이 안되고 여러분의 로컬서버에서만 접근 가능하다. 이것이 기본설정인 이유는 디버그모드상에서 어플리케이션의 사용자가 임의의 파이썬코드를 여러분의 컴퓨터에서 실행할 수 있기 때문이다.
여러분이 debug 모드를 해제하거나 여러분의 네트워크상에 있는 사용자들을 신뢰한다면, 다음과 같이 간단히 run() 메소드의 호출을 변경해서 서버의 접근을 오픈할 수 있다.

``` python
app.run(host='0.0.0.0') # 으로 작성, 디버그 모드와 함께 보낼 수 있다.
```

-----------------------------------------

> 라우팅
현대 웹 어플리케이션은 잘 구조화된 URL로 구성되있다. 이것으로 사람들은 URL을 쉽게 기억할 수 있고, 열악한 네트워크 연결 상황하의 기기들에서 동작하는 어플리케이션에서도 사용하기 좋다. 사용자가 인덱스 페이지를 거치지 않고 바로 원하는 페이지로 접근할 수 있다면, 사용자는 그 페이지를 좋아할 것이고 다시 방문할 가능성이 커진다.

위에서 본것처럼, route() 데코레이터는 함수와 URL을 연결해준다. 아래는 기본적인 예제들이다
``` python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
```
이 예제는 데코레이터의 인자가 다르므로, 각각 URL에 따라 다른 결과가 나오는 것을 확인 할 수 있다.

---------------------------------------------------------

> 변수 규칙
```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```
여기서 username은 문자열로, post_id는 정수로 사용됨을 확인 할 수 있다.

-----------------------------------------

> url_for

템플릿을 포함하여 응용 프로그램 전체에서 URL을 변경해야하는 오버 헤드를 방지하기 위해 URL을 만드는 데 사용됩니다. 

url_for없이 앱의 루트 URL에 변경이 있으면 링크가있는 모든 페이지에서 변경해야합니다.

이는 url의 주소를 모두 적지 않아도 된다는 장점으로 동적으로 URL을 만들 수 있다.

```python
@app.route('/index')
@app.route('/')
def index():
    return 'you are in the index page'
```
```html
<a href={{ url_for('index') }}>Index</a>
```
a 태그는 index url로 연결 된다.

> HTTP 메소드
HTTP(웹 어플리케이션에서 사용하는 프로토콜)는 URL 접근에 대해 몇가지 다른 방식을 제공한다. 

기본적으로 GET 방식으로 제공되지만, route() 데코레이터에 methods 인자를 제공하면 다른 방식으로 변경할 수 있다. 

아래에 몇가지 예가 있다
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```
methods가 POST이면 로그인 기능을 수행한다.

GET이면 수행할 필요가 없다.

----------------------------------------------

> 템플릿 보여주기

render_template()메소드를 이용하여 작성한 html파일(템플릿)을 보여준다.


```python
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```
템플릿을 찾는? 두 가지의 경우가 있다.

1. 모듈
<pre>
/application.py
/templates
    /hello.html
</pre>

2. 패키지
<pre>
/application
    /__init__.py
    /templates
        /hello.py
</pre>

---------------------------------

> request data

클라이언트에서 서버로 보내는 데이터를 처리하는데 사용되는 객체이다.

1. context local

Flask 에서 어떤 객체들은 보통 객체들이 아닌 전역 객체들이다. 이 객체들은 실제로 어떤 특정한 문맥에서 지역적인 객체들에 대한 대리자들이다. 무슨 말인지 어렵다. 하지만, 실제로는 꽤 쉽게 이해할 수 있다.

쓰레드를 다루는 문맥을 생각해보자. 웹에서 요청이 하나 들어오면, 웹서버는 새로운 쓰레드를 하나 생성한다 (그렇지 않다면, 다른 방식으로 기반을 이루는 객체가 쓰레드가 아닌 동시성을 제공하는 시스템을 다룰 수도 있다). 플라스크가 내부적으로 요청을 처리할때, 플라스크는 현재 처리되는 쓰레드를 활성화된 문맥이라고 간주하고, 현재 실행되는 어플리케이션과 WSGI환경을 그 문맥(쓰레드)에 연결한다. 이렇게 처리하는 것이 문맥을 지능적으로 처리하는 방식이고, 이렇게하여 한 어플리케이션이 끊어짐없이 다른 어플리케이션을 호출할 수 있다.

그렇다면 이것은 여러분에게 어떤 의미인가? 기본적으로 여러분이 유닛 테스트(Unit Test)와 같은 것을 하지 않는다면 이것을 완전히 무시할 수 있다. 여러분은 요청 객체에 의존하는 코드가 갑자기 깨지는것을 알게 될것인데, 왜냐하면 요청 객체가 존재하지 않기 때문이다. 해결책은 요청 객체를 생성해서 그 객체를 문맥에 연결하는 것이다. 유닛 테스트에 있어서 가장 쉬운 해결책은 test_request_context() 문맥 관리자(Context Manager)를 사용하는 것이다. with 절과 함께 사용해서 test_request_context() 문맥 관리자는 테스트 요청을 연결할 것이고, 그렇게해서 여러분은 그 객체와 상호 작용할 수 있다. 아래에 예가 있다:

```
요약) 플라스크는 내부적으로 요청을 처리할때 현재 처리되는 쓰레드를 활성화된 문맥이라고 간주하고 연결한다. -> 요청이 들어올 때 마다 기능을 수행한다. 그래서 요청이 들어오지 않으면 수행을 하지 않는다.

이는 기능을 수행하는 코드를 작성을 해도 요청이 들어오지 않으면 수행을 하지 않아서 버그를 찾는 유닛 테스트를 하기 힘든 환경인데, test_request_context() 문맥 관리자를 사용하여 테스트 요청을 보내어 기능을 확인 할 수 있다.
```
```python
from flask import request # request 객체 임포트

with app.test_request_context('/hello', method='POST'): 
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
```
?) with, assert에서 막힌다.
1. with 절
``` python
file_data = open('file.txt')
print(file_data.readline(), end="")
file_data.close()

↓

with open('file.txt') as file_data:
    # 기본적으로 사용하는 함수를  with문 안에 사용하면 되며
    # with문을 나올 때 close를 자동으로 불러줍니다.
    print(file_data.readline(), end="")
```
2. assert
뒤의 조건이 True가 아니면 AssertError를 발생시킨다.


이 외에는 프로젝트를 수행하면서 익히면 될 듯 하다.