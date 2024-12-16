from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import redis
import os

app = Flask(__name__)
CORS(app)

# Connect to Redis
def get_redis_connection():
    return redis.StrictRedis(
        host=os.getenv('REDIS_HOST', 'localhost'),
        port=os.getenv('REDIS_PORT', 6379),
        db=0,
        decode_responses=True
    )

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if the number has been checked before in Redis
def check_number_history(num):
    redis_conn = get_redis_connection()
    return redis_conn.exists(f'number:{num}')

# Function to save the number and whether it's prime in Redis
def save_number(num, is_prime_value):
    redis_conn = get_redis_connection()
    # Convert boolean to string and store
    redis_conn.hset(f'number:{num}', 'is_prime', str(is_prime_value))

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
