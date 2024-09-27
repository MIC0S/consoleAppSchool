import hashlib
import os

import psycopg2
import psycopg2.errors
import psycopg2.pool


class Database:
    def __init__(self):
        POSTGRES_USER = os.environ['POSTGRES_USER']
        POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
        POSTGRES_DATABASE = os.environ['POSTGRES_DATABASE']
        POSTGRES_HOST = os.environ['POSTGRES_HOST']
        POSTGRES_PORT = os.environ['POSTGRES_PORT']
        self.HASH_SALT = os.environ['HASH_SALT']
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            database=POSTGRES_DATABASE
        )

    def createUser(self, username, password):
        password_hashed = hashlib.sha224((password + self.HASH_SALT).encode()).hexdigest()
        conn = self.connection_pool.getconn()
        status = 0
        try:
            cursor = conn.cursor()
            cursor.execute(f'INSERT INTO users (username, password) VALUES(%s, %s);', (username, password_hashed))
            conn.commit()
        except psycopg2.errors.UniqueViolation:
            status = -1
        finally:
            self.connection_pool.putconn(conn)
        return status

    def authUser(self, username, password):
        password_hashed = hashlib.sha224((password + self.HASH_SALT).encode()).hexdigest()
        conn = self.connection_pool.getconn()
        try:
            cursor = conn.cursor()
            cursor.execute(f'SELECT password FROM users WHERE username=%s;', (username,))
            results = cursor.fetchone()
            if results is None:
                return False
            return password_hashed == results[0]
        finally:
            self.connection_pool.putconn(conn)
