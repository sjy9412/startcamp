import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # return '''Hello World!
    # <a href="/hi">반장 부르러가기</a>
    # <a href="/lotto">로또</a>
    # '''
    return render_template('hello.html')

@app.route('/hi')
def hi():
    # return '<h1>안녕</h1>'
    return render_template('hi.html')

# varialbe routing: 경로를 변수로 활용한다.
@app.route('/hi/<string:name>')
def higyo(name):
    # return f'<h1>{name} 안녕</h1>'
    return render_template('hi2.html',namee=name)

# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number**3}'

# /lunch/사람이름
@app.route('/lunch/<string:name>')
def lunch(name):
    menu = ['한식', '중식', '일식']
    menu2 = random.choice(menu)
    # return f'{name}, {menu2}먹어'
    return render_template('lunch.html',name=name, menu2=menu2)

# 로또
@app.route('/lotto')
def lotto():
    numbers = random.sample(range(1,46), 6)
    lotto = sorted(numbers)
    return f'이번주 당첨번호는 {lotto}입니다.'

if __name__ == '__main__':
    # python app.py를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)