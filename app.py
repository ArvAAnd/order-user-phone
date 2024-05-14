import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    users_list = [{'id': user['id'],
                   'name': user['name'],
                   'phone': user['phone'],
                   'order_name': user['order_name']}
                  for user in users]
    cursor.close()
    conn.close()
    return jsonify(users_list)

@app.route('/users_add', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    order_name = data.get('order_name')
    conn = get_db_connection()
    conn.execute('INSERT INTO users (name, phone, order_name) VALUES (?, ?, ?)',
                 (name, phone, order_name))
    conn.commit()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
