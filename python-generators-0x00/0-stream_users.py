import mysql.connector
from decimal import Decimal


# Generator function that streams users one by one
def stream_users():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ao5275/20@18",
            database="ALX_prodev",
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:  # Loop 1
            yield row

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


# Generator function that yields batches of users
def stream_users_in_batches(batch_size):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ao5275/20@18",
            database="ALX_prodev",
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        while True:  # Loop 2
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


# Process users over the age of 25 using batches
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):  # Loop 3
        filtered_users = (user for user in batch if Decimal(user["age"]) > 25)
        for user in filtered_users:
            print(f"{user['name']} ({user['email']}) is over 25 years old.")


# Example usage
if __name__ == "__main__":
    print("Streaming users one-by-one:")
    for user in stream_users():
        print(user)

    print("\nProcessing users over 25 in batches:")
    batch_processing(batch_size=5)
