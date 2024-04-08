print('#################################')
print('#################################')
print('#################################')
print(f'\n WELCOME TO BANK OF BALDWINS ')


#  check balance, deposit, withdraw, create account, delete account, modify account) and create tables for account data.

def user_balance():
    # retrieves data held in the 'balance' section of the user's profile
    balance = 0 ### Here should be where that data is being retrieved

def deposit(balance):
    additional_amount = input("How much would you like to deposit into your main account?")

    new_total_deposit = additional_amount + balance
    print(f'Your final balance after your deposit is ${new_total_deposit}')

def create_account():
    print("In order to create a new account, we will need some personal identifying information to associate with your account\n")

    birth_name = input("What is your ")
    new_username = input("Your username must be a minimum of 5 characters long (max #N characters):\n")

    new_password = input("Your password must be longer than 5 characters and shorter than #N characters:\n")

    new_username_characters = 0 # extract the number
    new_password_characters = 0 #extract this number
    new_user_varification(new_username_characters, new_password_characters, birth_name)


def new_user_varification(new_username_characters, new_password_characters, birth_name):
    if #5 =< new_username_characters =< #N characters:

        new_username_characters = True

    elif new_username_characters : False
    print("***YOU'VE SEEMED TO HAVE MADE AN ERROR IN YOUR SIGN-UP PAGE***")
    print("***YOUR NEW USERNAME DID NOT FIT WITHIN THE RANGE OF CHARACTERS ALLOWED FOR A NEW USERNAME, PLEASE TRY AGAIN.***")
    create_account()

    if 5 =< new_password_characters < #N characters:

        new_password_characters = True

    elif new_password_characters : False
    
    print("***YOU'VE SEEMED TO HAVE MADE AN ERROR IN YOUR SIGN-UP PAGE***")
    print("***YOUR NEW PASSWORD DID NOT FIT WITHIN THE RANGE OF CHARACTERS ALLOWED FOR A NEW PASSWORD, PLEASE TRY AGAIN.***")
    create_account()

    if (new_username_characters == True) & (new_password_characters == True):
        print(f'Welcome to BANK OF BALDWINS {birth_name}! We are delighted to have you as one of our new banking customers!')
        ## append user's birth_name, password and user name into the dataset.

def delete_account():
    print("It seems that you would like to delete your account from BANK OF BALDWINS... We are sad to let you go.")
    username = input("What is the username of your old account?")
    password = input("What is the password of your old account?")
    ## cycles through the database in order to find data if found using remove() most likely.



