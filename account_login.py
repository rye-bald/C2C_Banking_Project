import mysql.connector

from starting_page import welcome_page
# Global variable to store the logged-in username
username = None

def user_login():
    global username
    user_name_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    connection = None
    try:
        # Connect to MySQL using the MySQL extension
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Swarthmore2028',
            database='c2c_banking_data'
        )

        cursor = connection.cursor()

        # Check if the username and password match a row in the user_logins table
        query = "SELECT user_name, password FROM c2c_banking_data.user_logins WHERE user_name = %s AND password = %s"
        cursor.execute(query, (user_name_input, password_input))
        result = cursor.fetchone()

        if result:
            # Login successful
            username = user_name_input
            print("Login successful.")
        else:
            print("Incorrect username or password.")
            welcome_page()

    except mysql.connector.Error as e:
        print("MySQL Error:", e)

    except Exception as ex:
        print("Error:", ex)

    finally:
        try:
            if connection is not None and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed.")
        except Exception as ex:
            print("Error closing connection:", ex)

