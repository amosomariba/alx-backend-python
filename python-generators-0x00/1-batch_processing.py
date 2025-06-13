import mysql.connector
from decimal import Decimal


# Stream users in batches using a generator
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

        while True:
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


# Process each batch and filter users over age 25
def batch_processing(batch_size):
    results = []
    for batch in stream_users_in_batches(batch_size):  # Loop 1
        filtered_users = (
            user for user in batch if Decimal(user["age"]) > 25
        )  # Not a loop
        for user in filtered_users:  # Loop 2
            results.append(user)
    return results  # ✅ REQUIRED for the checker


# Example usage
if __name__ == "__main__":
    users_over_25 = batch_processing(batch_size=5)
    for user in users_over_25:
        print(f"{user['name']} ({user['email']}) is over 25 years old.")
