import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="mydb",
        user="admin",
        password="secret123",
        host="localhost",
        port="5432"
    )
