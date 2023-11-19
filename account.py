class Account:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def depo(self,amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Invalid deposit amount!")
            return False
        
    def withdrawl(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Invalid withdrawl amount!")
            return False
        
    
