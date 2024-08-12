# 환경셋팅
## set FLASK_APP=flask_basic.py (on win)
## export FLASK_APP=flask_basic.py (on linux/mac)

# 실행 명령
## flask -- app flask_basic.py run


from flask import Flask

app = Flask(__name__)

@app.route('/') # 루트로 들어왔을 때 실행되는 함수. 클라이언트가 url 다음에 루트로 아무것도 안쓰고 들어왔을 때 실행되는 함수 @는 데코레이터, 데코레이터 밑에 있는 함수를 실행시킨다.
def hello():
    # 여기다가 비즈니스 로직을 넣어준다.
    # 웹 데이터 수집
    # 데이터 처리
    # 데이터 저장
    # html 랜더링 하고 리턴
    return "<h1> 헬로 월드 !</h1>"

# if __name__ == '__main__':
#     app.run()