class BankAccount:
    def __init__(self, account_holder):
        """
        Initialize a new bank account with the given account_holder name.
        The balance should start at 0.0.
        """
        self.account_holder = account_holder
        self.balance = 0.0  # Initialize balance to 0.0

    def deposit(self, amount):
        """
        Increase the balance by the given amount.
        Assume amount is always a positive number.
        """
        # TODO: Add the deposit amount to the balance.
        pass

    def withdraw(self, amount):
        """
        Decrease the balance by the given amount if sufficient funds exist.
        If the amount is greater than the balance, print "Insufficient funds" and do nothing.
        """
        # TODO: Subtract the amount from balance if possible, otherwise print an error message.
        pass

    def get_balance(self):
        """
        Return the current balance.
        """
        # TODO: Return the current balance.
        pass
