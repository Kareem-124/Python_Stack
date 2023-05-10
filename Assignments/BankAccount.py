class BankAccount:
    def __init__(self, name, int_rate, balance=0):
        self.name = name
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds a 5$ feel will be deducted")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"The {self.name} Balance = {self.balance}")
        return self

    def yield_interests(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self
        else:
            print(
                f"The balance amount should not 0 or less / Current balance = {self.balance}")
            return self


kareem = BankAccount("Kareem", 0.01)
Zaid = BankAccount("Zaid", 0.02)

kareem.deposit(100).deposit(200).deposit(300).withdraw(100).yield_interests().display_account_info()
Zaid.deposit(200).deposit(300).withdraw(100).withdraw(100).withdraw(200).yield_interests().display_account_info()
