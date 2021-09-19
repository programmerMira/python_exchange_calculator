from flask import jsonify
from main import app
from calcularions import Calculations

calculator = Calculations()

#region get routes
@app.route('/api/addition/<first>/<second>', methods=['GET'])
def api_addition(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.addition(first,second)
    return jsonify(response_object)

@app.route('/api/substraction/<first>/<second>', methods=['GET'])
def api_substraction(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.substraction(first,second)
    return jsonify(response_object)

@app.route('/api/multiplication/<first>/<second>', methods=['GET'])
def api_multiplication(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.multiplication(first,second)
    return jsonify(response_object)

@app.route('/api/division/<first>/<second>', methods=['GET'])
def api_division(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.division(first,second)
    return jsonify(response_object)

@app.route('/api/percent/<first>/<second>', methods=['GET'])
def api_percent(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.percent(first,second)
    return jsonify(response_object)

@app.route('/api/power/<first>/<second>', methods=['GET'])
def api_power(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.power(first,second)
    return jsonify(response_object)

@app.route('/api/root/<first>/<second>', methods=['GET'])
def api_root(first,second):
    response_object = {'status': 'success'}
    response_object['data'] = calculator.root(first,second)
    return jsonify(response_object)