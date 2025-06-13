import sqlite3


# Class-based context manager for DB connection
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn  # This is what `with` assigns to the variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            print("[INFO] Database connection closed.")


# Using the context manager to fetch users
with DatabaseConnection("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print("Users:")
    for user in results:
        print(user)
