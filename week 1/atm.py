def main():
    balance = 0
    pin = "1234"  # Set a default PIN
    attempts = 0
    max_attempts = 3
    print("Welcome to the ATM!")
    
    while True:
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == pin:
            print("PIN accepted.")
            break
        else:
            attempts += 1
            print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")
            if attempts >= max_attempts:
                print("Maximum attempts reached. Exiting.")
                return

    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            # Check balance
            print(f"Your balance is: ${balance:.2f}")
            
        elif choice == '2':
            # Deposit money
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    balance += amount
                    print(f"Deposited ${amount:.2f}. New balance is ${balance:.2f}.")
                else:
                    print("Invalid amount. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif choice == '3':
            # Withdraw money
            try:
                if balance <= 0:
                    print("Insufficient funds. Your balance is $0.00.")
                    continue
                amount = float(input("Enter amount to withdraw: $"))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                elif amount > balance:
                    print("Insufficient funds.")
                else:
                    balance -= amount
                    print(f"Withdrew ${amount:.2f}. New balance is ${balance:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            # Exit the program
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")

# Run the program
main()