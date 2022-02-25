from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day10.dao_emp import DaoEmp

app = Flask(__name__)
de = DaoEmp()

@app.route('/hello')
def hello():
    return 'Hello World! Hello PYTHON!'

@app.route('/para')
def para():
    a = request.args.get('a')
    return 'para' + a

@app.route('/para_post', methods=['post'])
def para_post():
    # a = request.form['a']
    a = request.form.get('a')
    return 'para_post' + a

@app.route('/jsp')
def jsp():
    a = "12345"
    b = [1, 2, 3, 4, 5, 6]
    c = [
            {'e_id':'s001', 'e_name':'홍길동', 'age':6},
            {'e_id':'s002', 'e_name':'김길동', 'age':7},
            {'e_id':'s003', 'e_name':'박길동', 'age':8}
        ]
    d = de.select()
    return render_template('jsp.html', a=a, b=b, c=c, d=d)

if __name__ == '__main__':
    app.run()