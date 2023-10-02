from psycopg2 import OperationalError
import psycopg2


def connect_to_db(env):
    try:
        connection = psycopg2.connect(database=env["database"], user=env["username"],
                                      password=env["password"], host=env["host"], port=env["port"])
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM MovieInfo;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except OperationalError as e:
        print(f"L'erreur '{e}' s'est produite. La base de données n'est pas accessible.")
