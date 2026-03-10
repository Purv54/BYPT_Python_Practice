class BankAccount:

    def __init__(self , owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"BankAccount of {self.owner} with balance {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}")

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}")

Acc = BankAccount("Purv", 1000)
Om = BankAccount("Om", 1000)
Acc.deposit(500)
Acc.withdraw(1200)
print(Acc)
print(Om)