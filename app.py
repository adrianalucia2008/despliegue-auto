import os
from flask import Flask, jsonify

app = Flask(__name__)

DB_PASSWORD = "super_secret_password_12345"

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)