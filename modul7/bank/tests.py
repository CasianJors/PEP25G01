

def run_tests():
    # Test 1: Initial balance should be 0.0
    account = BankAccount("TestUser")
    assert account.get_balance() == 0.0, "Initial balance should be 0.0"

    # Test 2: After depositing 200, balance should be 200.0
    account.deposit(200)
    assert account.get_balance() == 200.0, "After depositing 200, balance should be 200.0"

    # Test 3: After withdrawing 150, balance should be 50.0
    account.withdraw(150)
    assert account.get_balance() == 50.0, "After withdrawing 150, balance should be 50.0"

    # Test 4: Attempt to withdraw 100 (insufficient funds)
    # The balance should remain unchanged and "Insufficient funds" should be printed.
    account.withdraw(100)
    assert account.get_balance() == 50.0, "Withdrawal with insufficient funds should not change the balance"

    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
