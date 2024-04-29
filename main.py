print('#################################')
print('#################################')
print('#################################')
print(f'\n WELCOME TO BANK OF BALDWINS ')

# from user_menu import user_main, user_balance, deposit
# from user_sign_upor_delete import create_account, delete_account, new_user_verification

# usermain()
from menu import user_main
# user_main()

from account_create import create_account, new_user_verification

# create_account()
import mysql.connector


from menu import user_main, get_balance_for_user, deposit

# Usage example

print(get_balance_for_user('davebald312'))
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

user_main()
