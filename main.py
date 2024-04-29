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
from menu import get_balance_for_user, deposit, withdraw


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

def user_main(username):
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            get_balance_for_user(username)
            print(f'Your current balance is ${get_balance_for_user(username):.2f}')
        elif choice == "2":
            deposit_amount_str = input(f'How much would you like to deposit today, {username}?')
            deposit_amount = int(deposit_amount_str)
            deposit(username, deposit_amount)
        elif choice == "3":
            withdraw_amount_str = input(f'How much would you like to withdraw today, {username}?')
            withdraw_amount = int(withdraw_amount_str)
            withdraw(username, withdraw_amount)
        elif choice == "4":
            print("Exiting the program. Thank you for using BANK OF BALDWIN!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

welcome_page()

user_main(username)
