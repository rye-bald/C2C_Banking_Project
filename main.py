print('#################################')
print('#################################')
print('#################################')
print(f'\n WELCOME TO BANK OF BALDWINS ')

# from user_menu import user_main, user_balance, deposit
# from user_sign_upor_delete import create_account, delete_account, new_user_verification

# usermain()

import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'user_logins_practice', password = 'Swarthmore2028')

connection.close()

