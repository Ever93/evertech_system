import psycopg2
from psycopg2 import pool
from app.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT


class Database:
    __connection_pool = None

    @staticmethod
    def initialize():
        Database.__connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
        )

    @staticmethod
    def get_connection():
        if Database.__connection_pool is None:
            Database.initialize()
        return Database.__connection_pool.getconn()

    @staticmethod
    def return_connection(conn):
        Database.__connection_pool.putconn(conn)

    @staticmethod
    def close_all():
        Database.__connection_pool.closeall()
