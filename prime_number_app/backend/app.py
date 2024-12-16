from flask import Flask, request, jsonify
from flask_cors import CORS 
import psycopg2
import math
import os

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', '/database/numbers.db'),
        database=os.getenv('DB_NAME', 'prime_numbers'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password')
    )
    return conn

# פונקציה לבדוק אם מספר ראשוני
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# פונקציה לחפש אם מספר כבר הוזן
def check_number_history(num):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM numbers WHERE num = %s", (num,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# שמירה במסד נתונים
def save_number(num, is_prime):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO numbers (num, is_prime) VALUES (%s, %s)", (num, is_prime))
    conn.commit()
    conn.close()

@app.route('/check_number', methods=['POST'])
def check_number():
    data = request.json
    num = data['num']
    
    is_prime_number = is_prime(num)
    number_exists = check_number_history(num)
    
    if not number_exists:
        save_number(num, is_prime_number)
    
    return jsonify({
        'is_prime': is_prime_number,
        'has_been_used': number_exists
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
