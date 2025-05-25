import sqlite3

# Connect to the database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Recreate the users table with an age column
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

# Insert sample users with age
cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", ("Alice", "alice@example.com", 30))
cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", ("Bob", "bob@example.com", 22))
cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", ("Charlie", "charlie@example.com", 35))

conn.commit()
conn.close()
print("Database initialized with age column and sample data.")
