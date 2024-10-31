class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0  # Initial balance is set to 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} units have been deposited. New balance: {
                  self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} units have been withdrawn. New balance: {
                      self.balance}")
            else:
                print("Insufficient funds to complete the withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"


my_account = BankAccount("987654")
print(my_account)  # Prints initial account information


my_account.deposit(287)

my_account.withdraw(131)

print("Current balance:", my_account.get_balance())

my_account.withdraw(500)

print(my_account)
