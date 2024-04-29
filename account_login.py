import mysql.connector

# Global variable to store the logged-in username
username = None

def user_login(username_input, password_input):
    global username
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
        query = "SELECT user_name FROM c2c_banking_data.user_logins WHERE user_name = %s AND password = %s"
        cursor.execute(query, (username_input, password_input))
        result = cursor.fetchone()

        if result:
            # Login successful
            username = username_input
            print("Login successful.")
        else:
            print("Incorrect username or password.")

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

def sign_in():
    user_name_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

