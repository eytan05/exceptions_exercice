import os
from db_connection import connect_to_db
from dotenv import load_dotenv


def get_env_val():
    load_dotenv(".env")
    return {
        "username": os.getenv('DB_USER'),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "database": os.getenv("DB_NAME"),
    }

if __name__ == '__main__':
    env_var = get_env_val()
    connect_to_db(env_var)
