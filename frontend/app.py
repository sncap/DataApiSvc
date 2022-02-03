import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(ROOT_PATH, 'dist')

app = Flask(__name__, static_folder=STATIC_PATH, static_url_path='')
CORS(app)


@app.route('/test/data', methods=['POST'])
def post_data():
    body = request.get_json()
    print(body)
    res = []
    res.append(body)
    return jsonify(res)


@app.route('/test/people', methods=['GET'])
def get_people():
    people = [{'name': 'Alice', 'birth-year': 1986},
              {'name': 'Bob', 'birth-year': 1985}]
    return jsonify(people)


@app.route('/test/company', methods=['GET'])
def get_company():
    company = [{'name': 'SDS', 'major': 'IT', 'parent': 'SAMSUNG'},
               {'name': 'CNS', 'major': 'IT', 'parent': 'LG'}]
    return jsonify(company)


@app.route('/')
def response_test():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(port=8080)
