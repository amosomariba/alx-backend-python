import sqlite3

# Connect to the database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
"""
)

# Insert sample data (optional, run only once)
cursor.execute(
    "INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com")
)
cursor.execute(
    "INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com")
)

# Commit and close
conn.commit()
conn.close()

print("Database setup complete.")
