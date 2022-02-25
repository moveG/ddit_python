from flask import Flask, jsonify
from flask.templating import render_template
from day11.dao_emp import DaoEmp
from flask.globals import request

app = Flask(__name__, static_url_path='', static_folder='static')
de = DaoEmp()

@app.route('/hello')
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)