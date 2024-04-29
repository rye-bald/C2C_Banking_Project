# check balance, deposit, withdraw, create account, delete account, modify account) and create tables for account data.
import mysql.connector

def create_account():
    print("In order to create a new account, we will need some personal identifying information to associate with your account.\n")

    sign_up_name = input("What is your birth name? ")
    new_username = input("Your username must be a minimum of 5 characters long: ")

    while len(new_username) < 5:
        print("*** Error: Your username must be at least 5 characters long. Please try again. ***")
        new_username = input("Your username: ")

    new_password = input("Your password must be longer than 5 characters: ")

    while len(new_password) <= 5:
        print("*** Error: Your password must be longer than 5 characters. Please try again. ***")
        new_password = input("Your password: ")

    new_email = input("What is your email address? ")
    employee_status = input("Are you an employee? Enter '1' for yes, '2' for no: ")

    while employee_status not in ['1', '2']:
        print("*** Error: Please enter either '1' for yes or '2' for no. ***")
        employee_status = input("Are you an employee? Enter '1' for yes, '2' for no: ")

    if employee_status == '1':
        new_account_type = 'Employee'
    else:
        new_account_type = 'Non-Employee'

    new_user_verification(new_username, new_password, sign_up_name, new_email, new_account_type)


def new_user_verification(new_username, new_password, sign_up_name, email, new_account_type):
    if len(new_username) >= 5 and len(new_password) > 5:
        print(f'Welcome to BANK OF BALDWINS, {sign_up_name}! We are delighted to have you as one of our new banking customers!')
        
        # Append user's sign_up_name, password, and username into the dataset or database
        add_account(new_username, new_password, sign_up_name, email, new_account_type)
    else:
        print("*** YOU'VE SEEMED TO HAVE MADE AN ERROR IN YOUR SIGN-UP PAGE ***")
        print("*** PLEASE ENSURE YOUR USERNAME HAS AT LEAST 5 CHARACTERS AND YOUR PASSWORD IS LONGER THAN 5 CHARACTERS. ***")
        create_account()



def add_account(new_username, new_password, sign_up_name, email, new_account_type):
    try:
        # Connect to MySQL using the MySQL extension
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Swarthmore2028',
            database='c2c_banking_data'
        )

        cursor = connection.cursor()

        # Insert new account data into the user_logins table
        query = "INSERT INTO c2c_banking_data.user_logins (sign_up_name, user_name, email, password, employee_type) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (sign_up_name, new_username, email, new_password, new_account_type))
        connection.commit()

        print("Account created successfully!")
        exit()
        
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

