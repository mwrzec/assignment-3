import random
from bank import Bank
from savings_account import SavingsAcc
from chequing_account import ChequingAcc

#class created to define application.
class Application:
    def __init__(self, bank):
        self.bank = bank
#def show_menu is made to display main menu for users allowing them to open accounts or select acounts and leave the application.
    def show_menu(self):
        while True:
            print("1. Select Account")
            print("2. Open Account")
            print("3. Exit Application")

            select = input("Enter your selection: ")

            if select == "1":
                account_num = input("Enter Account Number: ")
                account = self.bank.search_acc(account_num)

                if account:
                    print(f"Selected Account: {account_num}")
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
#Def show_acc_menu is also to show a menu for the user however this one is specific to the user account details.
    def show_acc_menu(self, account):
        while True:
            print("\nAccount Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit Account")

            select = input("Enter your selection: ")

            if select == "1":
                print(f"Balance: {account.get_balance()}")
            elif select == "2":
                amount = float(input("Enter the amount you want to deposit: "))
                account.deposit(amount)
                print("Deposit successful!")
            elif select == "3":
                amount = float(input("Enter the amount you want to withdraw: "))
                if account.withdraw(amount):
                    print("Withdrawal successful!")
                else:
                    print("Insufficient funds!")
            elif select == "4":
                print("Exiting Account Menu")
                break
            else:
                print("Invalid Selection. Try again.")
#def open_acc_menu is made to allow the user to create an account and is given a acc number after theyve specified account type and start balance.
    def open_acc_menu(self):
        acc_type = input("Enter account type (savings/chequing): ").lower()
        start_balance = float(input("Enter initial balance: "))

        if acc_type.lower() == "savings":
            account = SavingsAcc(
                str(random.randint(10000000, 99999999)), start_balance, 0)
        elif acc_type.lower() == "chequing":
            account = ChequingAcc(
                str(random.randint(10000000, 99999999)), start_balance, 0)
        else:
            print("Invalid account type. Please enter 'Savings' or 'Chequing'.")
            return

        self.bank.add_acc(account)
        print(
            f"Account opened successfully. Account Number: {account.acc_num}")


bank = Bank()
bank.create_def_acc()
app = Application(bank)


app.show_menu()
