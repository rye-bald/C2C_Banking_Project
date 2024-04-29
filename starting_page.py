
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