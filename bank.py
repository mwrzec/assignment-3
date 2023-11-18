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
        
