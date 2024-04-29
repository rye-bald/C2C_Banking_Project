# Assume the user has successfully logged in before reaching this point

def user_balance():
    # Retrieves data held in the 'balance' section of the user's profile
    balance = 0  # Placeholder for retrieving user's balance from the profile
    return balance

def deposit(balance):
    additional_amount = float(input("How much would you like to deposit into your main account? "))
    new_total_deposit = additional_amount + balance
    print(f'Your final balance after your deposit is ${new_total_deposit:.2f}')

def user_main():    
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            current_balance = user_balance()
            print(f'Your current balance is ${current_balance:.2f}')
        elif choice == "2":
            current_balance = user_balance()
            new_balance = deposit(current_balance)
            # Update the user's balance in the profile/database if needed
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")