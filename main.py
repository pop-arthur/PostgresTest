from db import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def add_user(name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    conn.close()

def list_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)
    conn.close()

# Simple CLI interaction
if __name__ == "__main__":
    create_table()
    # add_user("Mom", "mom@example.com")
    list_users()
