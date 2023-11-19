import random
from savings_account import SavingsAcc
from chequing_account import ChequingAcc
#class bank is created to define Bank
class Bank:
    def __init__(self):
        self.accounts = []
#def add_acc allows the user to add an account to their list.
    def add_acc(self, account):
        self.accounts.append(account)
#def search_acc allows the bank to search for the users account.
    def search_acc(self, acc_num):
        for account in self.accounts:
            if account.acc_num == acc_num:
                return account
        return None
#def create_acc_num allows the bank to assign the user a unique bank account number.
    def create_acc_num(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(random.randint(8, 12)))
#def create_def_acc allows the bank to create a default account.
    def create_def_acc(self):
        self.add_acc(ChequingAcc(self.create_acc_num(), 5000, 1000))
        self.add_acc(ChequingAcc(self.create_acc_num(), 7000, 1500))
        self.add_acc(SavingsAcc(self.create_acc_num(), 10000, 5000))
        self.add_acc(SavingsAcc(self.create_acc_num(), 15000, 6000))
        self.add_acc(SavingsAcc(self.create_acc_num(), 8000, 4000))
