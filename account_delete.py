
import mysql.connector

def delete_account():
    print("It seems that you would like to delete your account from BANK OF BALDWINS... We are sad to let you go.")
    username = input("What is the username of your old account? ")
    password = input("What is the password of your old account? ")

    try:
        # Connect to MySQL using the MySQL extension
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Swarthmore2028',
            database='c2c_banking_data'
        )

        cursor = connection.cursor()

        # Check if the user's account exists and matches the provided username and password
        query = "SELECT * FROM c2c_banking_data.user_logins WHERE user_name = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            # User's account found, proceed with deletion
            delete_query = "DELETE FROM c2c_banking_data.user_logins WHERE user_name = %s AND password = %s"
            cursor.execute(delete_query, (username, password))
            connection.commit()
            print("Your account has been successfully deleted.")
            welcome_page()
        else:
            print("No matching account found. Please check your username and password.")
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
