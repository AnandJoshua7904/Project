class bankaccount:
    def __init__(self,account_number,balance):
        self.__acoount_number=account_number
        self.__balance=balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance{self.__balance}"
        else:
            return "deposit must be positive"

    def withdraw(self, amount):
         if 0 < amount <= self.__balance:
             self.__balance -= amount
             return f"withdraw {amount}, New balance{self.__balance}"
         else:
             return "Insufficient balance or invalid amount."
         

    def get_balance(self):
              return f"current balance: {self.__balance}"
    
    def  get_account_number(self):
              return f"Account number: {self.__acoount_number}"
    

account= bankaccount("123534564547",1000 )

print(account.deposit(1500)) 
print(account.withdraw(300))
print(account.get_balance())
