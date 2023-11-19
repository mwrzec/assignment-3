from account import Account

class ChequingAcc(Account):
    def __init__(self, acc_num, balance, over_limit):
        super().__init__(acc_num, balance)
        self.over_limit = over_limit

    def withdrawl(self, amount):
        if amount > 0 and amount <= self.balance + self.over_limit:
            self.balance -= amount
            return True
        else:
            print("Withdrawlnot allowed. Exceeds overdraft limit.")
            return False