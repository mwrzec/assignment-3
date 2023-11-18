import random

class Bank:
    def __init__(self):
        self.accounts = []
    def add_acc(self, account):
        self.account.append(account)

    def search_acc(self, acc_num):
        for account in self.accounts:
            if account.acc_num == acc_num:
                return account
        return None
    
    def create_acc_num(self):
        return ''.join(str(random.randint(0,9)) for _ in range(random.randint(8,12)))
    
    def create_def_acc(self):
        self.add_acc(ChequingAcc(self.create_acc_num(),5000, 1000))
        self.add_acc(ChequingAcc(self.create_acc_num(),7000, 1500))
        self.add_acc(SavingsAcc(self.create_acc_num(),10000, 5000))
        self.add_acc(SavingsAcc(self.create_acc_num(),15000, 6000))
        self.add_acc(SavingsAcc(self.create_acc_num(),8000, 4000))