import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'PixelRealms',
    'raise_on_warnings': True
}

def connect():
    """Establish and return the database connection."""
    connection = mysql.connector.connect(**config)
    return connection

