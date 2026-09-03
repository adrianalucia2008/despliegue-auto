import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "API de Flask ejecutándose correctamente en Misión 1",
        "code": 200
    }), 200

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/db-check')
def db_check():
    conn = pymysql.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME'),
        connect_timeout=5
    )
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
    conn.close()
    return jsonify({"status": "connected", "result": result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)