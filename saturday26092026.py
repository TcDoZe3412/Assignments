class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance

    def withdrawal(self, withdraw):
        if self._balance >= withdraw:
            self._balance -= withdraw
            return self.get_balance()  # Added self. and return
        else:
            print("Insufficient Balance")


account = Bank("A", 100)
account.get_balance()
account.deposit(50)
print(account.get_balance())
account.withdrawal(30)
account.withdrawal(70)
print(account.get_balance())
account.withdrawal(70)
print(account.get_balance())
