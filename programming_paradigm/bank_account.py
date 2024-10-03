class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    #Depositing Method
    def deposit(self,amount):
        while True:
            """Looping thru the deposit function"""
            try:

                amount = float(input("Deposit: "))
                self.account_balance += amount
                print(f"Deposit: ${amount}")
                
            except ValueError as e:
                print(f"Invalid input {e}")  #Raising value error
    #Withdrawal Method
    def withdraw(self,amount):
        while True:
            """Looping thru the withdrawal function"""
            try:
                amount = float(input("Withdraw amount: "))
                if self.account_balance >= amount:
                    self.account_balance -= amount
                    print(f"Withdrew: ${amount}")
                    
                else:
                    print(f"Insufficient Funds {self.account_balance}")
            except ValueError as e:
                print(f"Invalid input, try again {e}") #Raising value error

    # Displaying current balance.
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
        

