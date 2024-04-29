print('#################################')
print('#################################')
print('#################################')
print(f'\n WELCOME TO BANK OF BALDWINS ')

# from user_menu import user_main, user_balance, deposit
# from user_sign_upor_delete import create_account, delete_account, new_user_verification
import mysql.connector

from account_create import create_account
from account_delete import delete_account
from account_login  import user_login
from menu import user_main, get_balance_for_user, deposit


def welcome_page():
    while True:

        print("Welcome to BANK OF BALDWINS!")
        print("Options:")
        print("1. Login")
        print("2. Create Account")
        print("3. Delete Account")
        print("4. Exit Program")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            user_login()
        elif choice == "2":
            create_account()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            print("Exiting the program. Thank you for using BANK OF BALDWIN!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            
welcome_page()
