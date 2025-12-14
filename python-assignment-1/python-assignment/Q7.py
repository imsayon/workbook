class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance # Encapsulated attribute

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}, New Balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance: print("Insufficient funds")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}, New Balance: {self._balance}")

    def show_balance(self):
        print(f"Account: {self.name}, Balance: {self._balance}")

acc = BankAccount("Alice", 1000)
acc.deposit(500); acc.withdraw(200); acc.show_balance()