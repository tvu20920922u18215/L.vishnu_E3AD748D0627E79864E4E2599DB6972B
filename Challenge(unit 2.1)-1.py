''' Implement a class called BankAccount that represents a bank account. The class should 
have private attributes for account number, account holder name, and account balance. Include 
methods to deposit money, withdraw money, and display the account balance. Ensure that the 
account balance cannot be accessed directly from outside the class. Write a program to create an 
instance of the BankAccount class and test the deposit and withdrawal functionality.'''

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"


# Testing the BankAccount class
if __name__ == "__main__":
    account = BankAccount("12345", "John Doe", 1000.0)

    print(account.display_balance())  # Display initial balance
    print(account.deposit(500.0))     # Deposit $500
    print(account.withdraw(200.0))    # Withdraw $200
    print(account.display_balance())  # Display updated balance
