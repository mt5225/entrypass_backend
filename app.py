#!/usr/bin/python
from flask import Flask, jsonify
from flask import request
import logging
from logging.handlers import RotatingFileHandler
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return "Hello, World!"

## curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://uinnova.com:9009/form
@app.route('/form', methods=['POST'])
def get_form_details():
    content = request.get_json()
    app.logger.info(content)
    return jsonify(content), 200

@app.route('/dummy_api', methods=['GET'])
def dummy_api():
    return jsonify(msg='okey'), 200

if __name__ == '__main__':
    LOG_FILENAME = 'form.log'
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler(LOG_FILENAME, maxBytes=10000000, backupCount=5)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    CORS(app)
    app.run(host='0.0.0.0', port=9009, debug=True)
