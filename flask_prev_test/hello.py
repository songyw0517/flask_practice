from flask import Flask, url_for, render_template, request
from flask import request
import google_keyword

app = Flask(__name__)
from markupsafe import escape
@app.route('/')
def helloWorld(name=None):
    #get을 통한 전달받은 데이터를 확인
    key1 = request.args.get('keyword1')
    key2 = request.args.get('keyword2')
    print(key1, key2)

    if not key1 or not key2: #빈 문자열은 거짓으로 판단하기때문에 이렇게 쓰면된다.
        return render_template('hello.html')
    else:
        # 모듈로 키워드 개수 가져오기
        value1 = google_keyword.get_keyword_number(key1)
        value2 = google_keyword.get_keyword_number(key2)

        # 사용자에게 보낼 데이터
        data = {key1:value1, key2:value2}

        return render_template('hello.html', data=data)

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)