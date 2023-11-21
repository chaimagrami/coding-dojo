class BankAccount:
    # don't forget to add some default values for these parameters!
    all_account=[]
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate=int_rate 
        self.balance=balance
        BankAccount.all_account.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
    # your code here
        self.balance+=amount
        return self

    def withdraw(self, amount):
        # your code here
        if amount<=self.balance :
            self.balance-=amount
        else : 
            print("insufficient funds: Charging a $5 fee")  
        return self 

    def display_account_info(self):
        # your code here
        print(f"Balance : ${self.balance}")
        return self
    def yield_interest(self):
        # your code here
        self.balance=self.balance+ self.balance*self.int_rate
        return self
    @classmethod
    def display_all_account(cls):
        for i in BankAccount.all_account :
            print(i.display_account_info())
        return None



acc1=BankAccount(0.01,30)
acc2=BankAccount()

print(BankAccount.display_all_account())

acc1.deposit(30).deposit(40).deposit(1000).withdraw(120).yield_interest().display_account_info()
acc2.deposit(40).deposit(1000).withdraw(120).withdraw(120).withdraw(120).withdraw(120).yield_interest().display_account_info()

print(BankAccount.display_all_account())