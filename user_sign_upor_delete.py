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
    else:
        print("*** YOU'VE SEEMED TO HAVE MADE AN ERROR IN YOUR SIGN-UP PAGE ***")
        print("*** PLEASE ENSURE YOUR USERNAME HAS AT LEAST 5 CHARACTERS AND YOUR PASSWORD IS LONGER THAN 5 CHARACTERS. ***")
        create_account()

def delete_account():
    print("It seems that you would like to delete your account from BANK OF BALDWINS... We are sad to let you go.")
    username = input("What is the username of your old account? ")
    password = input("What is the password of your old account? ")
    # Cycle through the database to find and delete the user's account if found


