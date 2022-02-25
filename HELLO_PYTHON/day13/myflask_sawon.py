from flask import Flask, jsonify
from flask.templating import render_template
from day13.dao_sawon import DaoSawon
from flask.globals import request

app = Flask(__name__, static_url_path='', static_folder='static')
de = DaoSawon()

@app.route('/sawon')
def ajax_list():
    mylist = de.select()
    return render_template('sawon.html', mylist=mylist)

@app.route('/ajax_insert', methods=['POST'])
def ajax_insert():
    data = request.get_json()

    s_name  = data["s_name"]
    age     = data["age"]
    address = data["address"]
    
    result = "ng"
    cnt = de.insert(s_name, age, address)
    if cnt == 1:
        result = "ok"
    
    return jsonify(result = result)

@app.route('/ajax_update', methods=['POST'])
def ajax_update():
    data = request.get_json()

    s_id    = data["s_id"]
    s_name  = data["s_name"]
    age     = data["age"]
    address = data["address"]
    
    result = "ng"
    cnt = de.update(s_id, s_name, age, address)
    if cnt == 1:
        result = "ok"
    
    return jsonify(result = result)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    data = request.get_json()

    s_id = data["s_id"]
    
    result = "ng"
    cnt = de.delete(s_id)
    if cnt == 1:
        result = "ok"
    
    return jsonify(result = result)
    
if __name__ == '__main__':
    app.run(debug=True)