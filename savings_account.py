from account import Account

class SavingsAcc(Account):
    def __init__(self, acc_num, balance, min_bal):
        super().__init__(acc_num, balance)
        self.min_bal = min_bal

    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= self.min_bal:
            self.balance -= amount
            return True
        else:
            print("Withdrawal not allowed. Exceeds minimum balance.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Invalid deposit amount.")
            return False