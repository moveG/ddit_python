from flask import Flask, jsonify
from flask.templating import render_template
from day11.dao_emp import DaoEmp
from flask.globals import request

app = Flask(__name__, static_url_path='', static_folder='static')
de = DaoEmp()

@app.route('/emp')
def emp():
    mylist = de.select()
    return render_template('emp.html', mylist=mylist)

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data)

    return jsonify(result = "success", result2= data)

if __name__ == '__main__':
    app.run(debug=True)