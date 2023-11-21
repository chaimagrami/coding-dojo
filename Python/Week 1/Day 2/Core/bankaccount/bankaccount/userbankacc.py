class VipAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self

    def display_info(self):
        print(f"Balance: {self.balance}")
        return self

class User:
    My_account = []

    def __init__(self, name, email, vipAcc):
        self.name = name
        self.email = email
        self.vipAcc = vipAcc

    def deposit(self, amount):
        self.vipAcc.deposit(amount)
        return self

    def withdraw(self, amount):
        self.vipAcc.withdraw(amount)
        return self

    def display_My_account(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        self.vipAcc.display_info()
        return self


vip_account = VipAccount()
ChaimaGrami = User("Chaima Grami", "Chaima@example.com", vip_account)
ChaimaGrami.deposit(3211).deposit(756443).deposit(21212).deposit(3494).display_My_account()
ChaimaGrami.withdraw(3211).withdraw(2443).withdraw(14212).withdraw(3494).display_My_account()