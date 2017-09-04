#!/usr/bin/python
import sqlite3
import logging
from flask import Flask, jsonify
from logging.handlers import RotatingFileHandler
from flask_cors import CORS


app = Flask(__name__, static_url_path='', static_folder='static')
conn = sqlite3.connect('./entrypass.db')
cur = conn.cursor()

def clean_db():
    cur.execute("DELETE FROM live")
    conn.commit()


@app.route('/')
def index():
    return jsonify(msg='Hello, World!'), 200


@app.route('/dummy_api', methods=['GET'])
def dummy_api():
    return jsonify(msg='okey'), 200

@app.route('/doorstatus', methods=['GET'])
def doorstatus():
    msg = {}
    msg_short = "" 
    try:
        cur.execute("SELECT rowid,* FROM live ORDER BY ROWID DESC LIMIT 1")
        data = cur.fetchone()
        msg=dict(zip(['ROWID', 'ETYPE','TRDATE','TRTIME','TRCODE','TRDESC', 'TRID', 'DEVNAME'], [x for x in data]))
        msg_short="{0}:{1}".format(data[7],data[4])  
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
    return msg_short, 200

if __name__ == '__main__':
    clean_db()
    LOG_FILENAME = './entrypass_api.log'
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler(LOG_FILENAME, maxBytes=10000000, backupCount=5)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    CORS(app)
    app.run(host='0.0.0.0', port=9009, debug=True)
