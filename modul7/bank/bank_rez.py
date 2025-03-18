class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def transfer(self, cont, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            cont.deposit(amount)
        else:
            print('error')

