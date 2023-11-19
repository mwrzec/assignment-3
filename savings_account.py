from account import Account
#class savingsacc is make to define savings account and assist in the simulation of a bank account.
class SavingsAcc(Account):
    def __init__(self, acc_num, balance, min_bal):
        super().__init__(acc_num, balance)
        self.min_bal = min_bal
#def withdraw is used to simulate the withdrawl of money on the users simulated savings account.
    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= self.min_bal:
            self.balance -= amount
            return True
        else:
            print("Withdrawal not allowed. Exceeds minimum balance.")
            return False
#def deposit is used to simulate the deposit of money on the users simulated savings account.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Invalid deposit amount.")
            return False