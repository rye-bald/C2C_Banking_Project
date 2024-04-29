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


from starting_page import welcome_page

welcome_page()
