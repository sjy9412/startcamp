# 0. flask 패키지 가져오기
import random
from flask import Flask, render_template, request

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route("/lunch")
def lunch():
    menus = ['레드코코넛누들', '소불고기', '삼계탕', '싸이버거', '치킨']
    pick = random.choice(menus)
    return render_template('lunch.html', menus=menus, pick=pick)

@app.route("/naver")
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # 사용자가 보낸 데이터를 받아와서
    text = request.args.get('say')
    text2 = request.args.get('say2')
    # 템플릿에 넘겨준다.
    return render_template('pong.html', text=text, text2=text2)

@app.route('/lck')
def lck():
    return render_template('lck.html')

@app.route('/random_lck')
def random_lck():
    name = request.args.get('name')
    choice = request.args.get('team')
    if choice == 'team1':
        team = ['KZ','AF','GRF','SB']
    else:
        team = ['T1','GEN','KT']
    pick_lck = random.choice(team)
    image = f'{pick_lck}.png'
    return render_template('random_lck.html', name=name, pick=pick_lck, img=image)

@app.route('/random')
def random_game():
    return render_template('random.html')

@app.route('/result')
def result():
    weather = request.args.get('weather')
    mood = request.args.get('mood')
    return render_template('result.html',    weather=weather, mood=mood)

@app.route('/lotto')
def lotto():
    return render_template('lotto.html')

@app.route('/lotto_result')
def lotto_result():
    name = request.args.get('name')
    num = request.args.get('num')
    random.seed(num)
    numbers = random.sample(range(1,46),6)
    return render_template('lotto_result.html', name=name, numbers=numbers )


if __name__ == '__main__':
    app.run(debug=True)
