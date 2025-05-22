import mysql.connector
from decimal import Decimal

# Stream users in batches using a generator
def stream_users_in_batches(batch_size):
    try:
        # Connect to ALX_prodev database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',        # Replace with your MySQL username
            password='Ao5275/20@18',    # Replace with your MySQL password
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch  # Yield each batch of users

    except mysql.connector.Error as err:
        print(f" Database Error: {err}")
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass

# Process each batch and filter users over age 25
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):  # Loop 1
        filtered_users = (user for user in batch if Decimal(user['age']) > 25)  # Generator expression (not a loop)
        for user in filtered_users:  # Loop 2
            print(f" {user['name']} ({user['email']}) is over 25 years old.")

# Example usage
if __name__ == "__main__":
    batch_processing(batch_size=5)
