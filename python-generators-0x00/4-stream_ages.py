import mysql.connector
from decimal import Decimal, getcontext


# Generator to stream user ages one by one
def stream_user_ages():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ao5275/20@18",
            database="ALX_prodev",
        )
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        for (age,) in cursor:  # Loop 1
            yield Decimal(age)

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


# Calculate average age using the generator
def calculate_average_age():
    total_age = Decimal(0)
    count = 0

    for age in stream_user_ages():  # Loop 2
        total_age += age
        count += 1

    if count > 0:
        average = total_age / count
        print(f"Average age of users: {average}")
    else:
        print("No users found.")


# Run the calculation
if __name__ == "__main__":
    calculate_average_age()
