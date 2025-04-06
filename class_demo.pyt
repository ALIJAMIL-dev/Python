# Bank Application
# acc = BankAccount("John Doe")
# acc.deposit => 0
# acc.deposit(100) => 100.0
# acc.withdraw(50) => 50.0

class BankAccount: 
    def __init__(self, name: str, balance: float = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Withdrawal amount must be positive and less than or equal to the balance.")