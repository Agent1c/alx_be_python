class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    #Depositing Method
    def deposit(self,amount):
        # while True:
            """prompting user for deposit function"""
            try:
                if amount > 0:
                    self.account_balance += amount
                    return True
                    
            except ValueError as e:
                print(f"Invalid input {e}")  #Raising value error
                return False
            
    #Withdrawal Method
    def withdraw(self,amount):
        # evaluating user requests.
            """prompting user for withdrawal function"""
            try:
                if amount > 0:
                    if amount <= self.account_balance:
                        self.account_balance -= amount
                        return True
            except ValueError as e:
                print(f"Invalid input, try again {e}") #Raising value error
            else:
                return False

    # Displaying current balance.
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
        

