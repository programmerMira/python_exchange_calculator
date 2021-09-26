from flask import Flask, jsonify, request
from flask_cors import CORS

from calcularions import Calculations

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

calculator = Calculations()

# enable CORS
CORS(app)

@app.route('/api', methods=['GET','POST'])
def hello():
    response_object = {'status': 'success'}
    response_object['data'] = "Start using server!"
    response_object['info'] = "/api/help for more details"
    if flask.request.method=='POST':
        expression = request.get_json()
        response_object['result'] = str(eval(expression['expression'],{},{}))
    return jsonify(response_object)

#region get routes
@app.route('/',method=['GET']
def help():
    response_object = {'status': 'success'}
    response_object['/api'] = "post method with json: {'expression':'2-3+7...'}, returns json: {...'result':'number',...}"
    response_object['addition'] = "get method, url: /api/addition/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['substraction'] = "get method, url: /api/substraction/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['multiplication'] = "get method, url: /api/multiplication/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['division'] = "get method, url: /api/division/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['percent'] = "get method, url: /api/percent/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['power'] = "get method, url: /api/power/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['root'] = "get method, url: /api/root/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    return jsonify(response_object)

@app.route('/api/addition/<first>/<second>', methods=['GET'])
def api_addition(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.addition(first,second)
    response_object['info'] = "/api/help for more details"
    return jsonify(response_object)

@app.route('/api/substraction/<first>/<second>', methods=['GET'])
def api_substraction(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.substraction(first,second)
    response_object['info'] = "/api/help for more details"
    return jsonify(response_object)

@app.route('/api/multiplication/<first>/<second>', methods=['GET'])
def api_multiplication(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.multiplication(first,second)
    response_object['info'] = "/api/help for more details"
    return jsonify(response_object)

@app.route('/api/division/<first>/<second>', methods=['GET'])
def api_division(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.division(first,second)
    response_object['info'] = "/api/help for more details"
    return jsonify(response_object)

@app.route('/api/percent/<first>/<second>', methods=['GET'])
def api_percent(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.percent(first,second)
    response_object['info'] = "/api/help for more details"
    return jsonify(response_object)

@app.route('/api/power/<first>/<second>', methods=['GET'])
def api_power(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.power(first,second)
    response_object['info'] = "/api/help for more details"
    return jsonify(response_object)

@app.route('/api/root/<first>/<second>', methods=['GET'])
def api_root(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.substraction(first,second)
    response_object['info'] = "/api/help for more details"
    return jsonify(response_object)

@app.route('/api/help', methods=['GET'])
def help_1():
    response_object = {'status': 'success'}
    response_object['/api'] = "post method with json: {'expression':'2-3+7...'}, returns json: {...'result':'number',...}"
    response_object['addition'] = "get method, url: /api/addition/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['substraction'] = "get method, url: /api/substraction/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['multiplication'] = "get method, url: /api/multiplication/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['division'] = "get method, url: /api/division/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['percent'] = "get method, url: /api/percent/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['power'] = "get method, url: /api/power/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    response_object['root'] = "get method, url: /api/root/<first_number>/<second_number>, returns json: {...'result':'number',...}"
    return jsonify(response_object)
#endregion