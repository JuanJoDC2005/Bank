from BankLibrary import BankAccount


def chatbot():
    print("Welcome to the Bank Account Chatbot!")

    # Create a bank account instance
    account_number = input(
        "Enter a unique account number for your new account: ")
    account = BankAccount(account_number)
    print(f"Account created with account number: {account.account_number}")

    while True:
        print("\nOptions: 'deposit', 'withdraw', 'balance', 'exit'")
        action = input("What would you like to do? ").lower()

        if action == 'deposit':
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))

        elif action == 'withdraw':
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))

        elif action == 'balance':
            print(f"Current balance: {account.get_balance()}")

        elif action == 'exit':
            print("Thank you for using the Bank Account Chatbot. Goodbye!")
            break

        else:
            print(
                "Invalid option. Please choose from 'deposit', 'withdraw', 'balance', or 'exit'.")


# Run the chatbot
if __name__ == "__main__":
    chatbot()
