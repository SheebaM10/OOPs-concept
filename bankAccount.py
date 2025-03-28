# Create a Class for a Bank Account Attributes: account_holder, balance Methods: deposit(amount), withdraw(amount), display_balance()
 
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount< self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")
    
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")


account = BankAccount("Sheeba", 1000)
account.deposit(400)
account.withdraw(1500)
account.display_balance()
