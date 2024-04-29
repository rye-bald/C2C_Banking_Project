#  check balance, deposit, withdraw, create account, delete account, modify account) and create tables for account data.

def create_account():
    print("In order to create a new account, we will need some personal identifying information to associate with your account.\n")

    birth_name = input("What is your birth name? ")
    new_username = input("Your username must be a minimum of 5 characters long: ")

    while len(new_username) < 5:
        print("*** Error: Your username must be at least 5 characters long. Please try again. ***")
        new_username = input("Your username: ")

    new_password = input("Your password must be longer than 5 characters: ")

    while len(new_password) <= 5:
        print("*** Error: Your password must be longer than 5 characters. Please try again. ***")
        new_password = input("Your password: ")

    new_user_verification(new_username, new_password, birth_name)

def new_user_verification(username, password, birth_name):
    if len(username) >= 5 and len(password) > 5:
        print(f'Welcome to BANK OF BALDWINS, {birth_name}! We are delighted to have you as one of our new banking customers!')
        
        # Append user's birth_name, password, and username into the dataset or database
        add_account(username, password, birth_name)
    else:
        print("*** YOU'VE SEEMED TO HAVE MADE AN ERROR IN YOUR SIGN-UP PAGE ***")
        print("*** PLEASE ENSURE YOUR USERNAME HAS AT LEAST 5 CHARACTERS AND YOUR PASSWORD IS LONGER THAN 5 CHARACTERS. ***")
        create_account()


import mysql.connector

def add_account(username, password, birth_name):
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
        query = "INSERT INTO c2c_banking_data.user_logins (user_name, password, birth_name) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password, birth_name))
        connection.commit()

        print("Account created successfully!")
        
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
