import sqlite3

DB_PATH = "database.sqlite"

def connect_db(db_path=DB_PATH):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_db():
    conn = connect_db()
    if conn:
        try:
            script = "scheme.sql"
            with open(script, "r") as file:
                conn.executescript(file.read())
            conn.commit()
        except Exception as e:
            print(f"Error creating database: {e}")
        finally:
            conn.close()

def db_execute(command, params=None, path=DB_PATH):
    conn = connect_db(path)
    if conn:
        try:
            # Pokud params není None, použijeme ho, jinak prázdný tuple
            result = conn.execute(command, params or ()).fetchall()
            conn.commit()
            return result
        except sqlite3.Error as e:
            print(f"Error executing command: {e}")
            return None
        finally:
            conn.close()
