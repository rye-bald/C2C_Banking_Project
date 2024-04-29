def welcome_page():
    print("Welcome to BANK OF BALDWINS!")
    print("Options:")
    print("1. Login")
    print("2. Create Account")
    print("3. Delete Account")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        user_login()
    elif choice == "2":
        create_account()
    elif choice == "3":
        delete_account()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")