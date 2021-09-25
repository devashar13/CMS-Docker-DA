from datetime import datetime

import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True
results = []


@app.route("/", methods=["GET"])
def home():
    if not results:
        response = dict(message="Most recent value not available")
    else:
        response = results[-1]
    return response, 200


@app.route("/recentresults", methods=["GET"])
def recent_results():
    return jsonify(results[-10:][::-1]), 200


@app.route("/allresults", methods=["GET"])
def all_results():
    return jsonify(results), 200


@app.route("/operate", methods=["POST"])
def operate():
   
    operation = request.json.get('calculation')
    print(operation)
    result = 0
    try:
        if "+" in operation:
            operatee = operation.split("+")
            result = int(operatee[0]) + int(operatee[1])
        if "-" in operation:
            operatee = operation.split("-")
            result = int(operatee[0]) - int(operatee[1])
        if "*" in operation:
            operatee = operation.split("*")
            result = int(operatee[0]) * int(operatee[1])
        if "/" in operation:
            operatee = operation.split("/")
            result = int(operatee[0]) / int(operatee[1])
        response = {"updated_date": datetime.now(), "operation": operation, "result": result}
        results.append(response)
        return response, 200
    except Exception as e:
        return dict(error="Calculation Error", exception=str(e), message="Review operation parameters and try again"), 400



if __name__ == "__main__":
    app.run(host="0.0.0.0")