import psycopg2
import os

def create_tables():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'prime_numbers'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password')
    )
    
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS numbers (
            id SERIAL PRIMARY KEY,
            num INTEGER UNIQUE,
            is_prime BOOLEAN
        );
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
