import mysql.connector
import csv
import uuid
from mysql.connector import errorcode


# Prototype: Connects to the MySQL server
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="Ao5275/20@18",  # Replace with your MySQL password
        )
        print(" Connected to MySQL Server.")
        return conn
    except mysql.connector.Error as err:
        print(f" Error connecting to MySQL: {err}")
        exit(1)


# Prototype: Creates the database ALX_prodev if it does not exist
def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print(" Database ALX_prodev is ready.")
    except mysql.connector.Error as err:
        print(f" Failed creating database: {err}")
    finally:
        cursor.close()


# Prototype: Connects to the ALX_prodev database
def connect_to_prodev():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="Ao5275/20@18",  # Replace with your MySQL password
            database="ALX_prodev",
        )
        print(" Connected to ALX_prodev database.")
        return conn
    except mysql.connector.Error as err:
        print(f" Error connecting to ALX_prodev: {err}")
        exit(1)


# Prototype: Creates a table user_data with the required fields
def create_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(5,2) NOT NULL,
                INDEX (user_id)
            )
        """
        )
        print(" Table user_data is ready.")
    except mysql.connector.Error as err:
        print(f" Failed creating table: {err}")
    finally:
        cursor.close()


# Prototype: Inserts data into the table if it does not already exist
def insert_data(connection, data):
    cursor = connection.cursor()
    for row in data:
        name, email, age = row
        user_id = str(uuid.uuid4())
        try:
            # Check if email already exists to avoid duplicates
            cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
            if cursor.fetchone():
                print(f" Skipping duplicate: {email}")
                continue

            cursor.execute(
                """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """,
                (user_id, name, email, float(age)),
            )
            print(f" Inserted: {name} - {email}")
        except mysql.connector.Error as err:
            print(f" Error inserting {email}: {err}")
    connection.commit()
    cursor.close()


# Read CSV data
def read_csv(filename):
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        return list(reader)


# Main driver
if __name__ == "__main__":
    base_conn = connect_db()
    create_database(base_conn)
    base_conn.close()

    db_conn = connect_to_prodev()
    create_table(db_conn)

    data = read_csv("user_data.csv")
    insert_data(db_conn, data)
    db_conn.close()
