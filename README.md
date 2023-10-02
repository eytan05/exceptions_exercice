# PostgreSQL Database Connection and Query Execution

This script demonstrates how to connect to a PostgreSQL database, execute a basic SQL query, handle exceptions, and close the connection using the `psycopg2` library in Python.

## Dependencies

- Python 3.x
- psycopg2-binary
- python-dotenv
You can install `psycopg2-binary` using pip:

```bash
pip install psycopg2-binary
pip install python-dotenv
```

## Usage

1. Ensure that your PostgreSQL server is running and accessible.
Create a .env file in the same directory as your script with the following content:
``
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_localhost
DB_PORT=your_port
``
2. Ensure that your PostgreSQL server is running and accessible.
3. Update the database connection parameters in the script (`database`, `user`, `password`, `host`, `port`) to match your PostgreSQL setup.
4. Run the script:

```bash
python main.py
```

## Troubleshooting

If the script is unable to connect to the database, ensure that:

- The PostgreSQL server is running.
- The connection parameters in the script are correct.
- The specified database exists and the user has the necessary permissions.
- Network and firewall settings allow connections to the PostgreSQL server.