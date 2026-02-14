class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

b, w = map(int, input().split())

acc = Account("", b)

if not acc.withdraw(w):
    print("Insufficient Funds")
else:
    print(acc.balance)