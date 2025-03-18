from bank import BankAccount


account = BankAccount("Alice")


account.deposit(150)
account.withdraw(50)


print(account.get_balance())  # Expected output: 100.0

account.withdraw(200)         # Should print "Insufficient funds" and balance remains 100.0
