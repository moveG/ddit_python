from flask import Flask, jsonify
from flask.templating import render_template
from dao_emp import DaoEmp
from flask.globals import request

app = Flask(__name__, static_url_path='', static_folder='static')
de = DaoEmp()

@app.route('/emp')
def emp():
    mylist = de.select()
    return render_template('emp.html', mylist=mylist)

@app.route('/ajax_insert', methods=['POST'])
def ajax_insert():
    data = request.get_json()
    
    e_id   = data["e_id"]
    e_name = data["e_name"]
    age    = data["age"]
    sex    = data["sex"]
    tel    = data["tel"]
    
    result = "ng"
    cnt = de.insert(e_id, e_name, age, sex, tel)
    if cnt == 1:
        result = "ok"
    
    return jsonify(result = result)

@app.route('/ajax_update', methods=['POST'])
def ajax_update():
    data = request.get_json()

    e_id   = data["e_id"]
    e_name = data["e_name"]
    age    = data["age"]
    sex    = data["sex"]
    tel    = data["tel"]
    
    result = "ng"
    cnt = de.update(e_id, e_name, age, sex, tel)
    if cnt == 1:
        result = "ok"
    
    return jsonify(result = result)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    data = request.get_json()

    e_id = data["e_id"]
    
    result = "ng"
    cnt = de.delete(e_id)
    if cnt == 1:
        result = "ok"
    
    return jsonify(result = result)
    
if __name__ == '__main__':
    app.run(debug=True)