import mysql.connector


# Fetches a specific page of users from the database
def paginate_users(page_size, offset):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ao5275/20@18",
            database="ALX_prodev",
        )
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        return cursor.fetchall()

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return []
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass


# Generator that lazily paginates users
def lazy_paginate(page_size):
    offset = 0
    while True:  # Only one loop
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size


# Example usage
if __name__ == "__main__":
    for page in lazy_paginate(3):
        print(f"\nNew Page (size {len(page)}):")
        for user in page:
            print(f"{user['name']} - {user['email']} - Age: {user['age']}")
