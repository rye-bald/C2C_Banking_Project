# Assume the user has successfully logged in before reaching this point
import mysql.connector

def get_balance_for_user(username):
    connection = None
    balance = None
    try:
        # Connect to MySQL using the MySQL extension in VS Code
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Swarthmore2028',
            database='c2c_banking_data'
        )

        cursor = connection.cursor()

        # Execute the SELECT query to fetch the balance for the user
        query = "SELECT checking_account_main FROM c2c_banking_data.user_logins WHERE user_name = %s"
        cursor.execute(query, (username,))

        # Fetch the result (if any)
        result = cursor.fetchone()

        # Check if the result is not None (i.e., user exists)
        if result:
            balance = result[0]  # Assuming checking_account_main is the first column in the result
        else:
            print("User not found.")

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

    return balance

def deposit(username, deposit_amount):
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

        # Fetch the current balance for the specified user
        query_select = "SELECT checking_account_main FROM c2c_banking_data.user_logins WHERE user_name = %s"
        cursor.execute(query_select, (username,))
        result = cursor.fetchone()

        if result:
            current_balance = result[0]
            new_balance = current_balance + deposit_amount

            # Update the checking_account_main column with the new balance
            query_update = "UPDATE c2c_banking_data.user_logins SET checking_account_main = %s WHERE user_name = %s"
            cursor.execute(query_update, (new_balance, username))
            connection.commit()

            print(f"Deposit of ${deposit_amount:.2f} successful. Your new balance is ${new_balance:.2f}")
        else:
            print(f"User with username {username} not found.")

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


def user_main(username):    
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            get_balance_for_user(username)
            print(f'Your current balance is ${get_balance_for_user(username):.2f}')
        elif choice == "2":
            deposit_amount = input(f'How much would you like to deposit today, {username}?')
            deposit(username, deposit_amount)
            # Update the user's balance in the profile/database if needed
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")