
class BankAccount:
    def __init__(self, owner, balance): #constructor
        self.owner = owner              #attribute
        self.balance = balance          #attribute

    def deposit(self, amount):          #method
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount

    def get_balance(self):
        return f"Owner: {self.owner} | Balance: ${self.balance}"

account = BankAccount("Ana", 1000)   #creating object
account.deposit(500)
account.withdraw(200)
print(account.get_balance())