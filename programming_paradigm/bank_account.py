class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    #Depositing Method
    def deposit(self,amount):
        # while True:
            """Looping thru the deposit function"""
            try:

                # amount = float(input("Deposit: "))
                self.account_balance += amount
                print(f"Deposit: ${amount}")
                # break
            except ValueError as e:
                print(f"Invalid input {e}")  #Raising value error
    #Withdrawal Method
    def withdraw(self,amount):
        # while True:
            """Looping thru the withdrawal function"""
            try:
                # amount = float(input("Withdraw amount: "))
                if amount <= self.account_balance:
                    self.account_balance -= amount
                    print(f"Withdrew: ${amount}")
                    return True
                else:
                    print(f"Insufficient Funds")
                    return False
            except ValueError as e:
                print(f"Invalid input, try again {e}") #Raising value error

    # Displaying current balance.
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
        

