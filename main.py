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

from account_create import create_account, new_user_verification, add_account

from account_delete import delete_account

from account_login import user_login

from starting_page import welcome_page

welcome_page()
