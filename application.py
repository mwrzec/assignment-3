import random
from bank import Bank
from savings_account import SavingsAcc
from chequing_account import ChequingAcc

class Application:
    def __init__(self,bank):
        self.bank = bank

    def show_menu(self):
        while True:
            print("1. Select Account")
            print("2. Open Account")
            print("3. Exit Application")

            select = input("Enter your selection: ")

            if select == "1":
                accountnum = input("Enter Account Number: ")
                account = self.bank.searchacc(accountnum)
                
                if account: 
                    print(f"Selected Account: {accountnum}")
                    self.show_acc_menu(account)

                else:
                    print("Account not found! ")
            elif select == "2":
                self.open_acc_menu()

            elif select == "3":
                print("You have exited the application. Goodbye!")
                break
            else:
                print("Invalid Selection. Try again.")
    def show_acc_menu(self,account):
        while True:
            print("\nAccount Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdrawl Money")
            print("4. Exit Account")

            select = input("Enter your selection: ")

            if select == "1":
                print(f"Balance: {account.balance()}")

            elif select == "2":
                amount = float(input("Enter the amount you want to deposit: "))
                account.depo(amount)
                print("Deposit sucessful!")

            elif select == "3":
                amount = float("Enter the amount you want to withdrawl: ")
                if account.withdrawl(amount):
                    print("Withdrawl sucessful!")

                else:
                    print("Insufficient funds!")

            elif select == "4":
                print("Exiting Account Menu")
                break
            else:
                print("Invalid Selection. Try again.")
    def open_acc_menu(self):
        acc_type = input("Enter the type of account you would like to open (Savings/Chequing): ").lower()
        start_balance = float(input("Enter start balance: "))

        if acc_type == "Savings":
            account = SavingsAcc(str(random.randint(10000000,99999999)), start_balance,0)
        elif acc_type == "Chequing":
            account = ChequingAcc(str(random.randint(10000000,99999999)), start_balance, 0)
        else:
            print("Invalid account type. Enter 'Chequing' or 'Savings'.")
            return
        self.bank.add_acc(account)
        print(f"Account has been opened successfuly! Account number: {account.acc_num}")

bank = Bank()
bank.create_def_acc()

app = Application(bank)

app.show_acc_menu()






