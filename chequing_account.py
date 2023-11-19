from account import Account
#Class ChequingAcc is made to define ChequingAcc and assist in the simulation of a bank account.
class ChequingAcc(Account):
    def __init__(self, acc_num, balance, over_limit):
        super().__init__(acc_num, balance)
        self.over_limit = over_limit
#def withdraw is used to simulate the withdrawl of money from a users simulated chequing account.
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.over_limit:
            self.balance -= amount
            return True
        else:
            print("Withdrawal not allowed. Exceeds overdraft limit.")
            return False
