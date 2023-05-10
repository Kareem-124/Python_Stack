class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)


class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = {
            "Account1": 0,
            "Account2": 0
        }
        self.int_rate = int_rate

    def deposit(self, amount, account):
        self.balance[account] += amount
        return self

    def withdraw(self, amount, account):
        if amount > self.balance[account]:
            print("Insufficient funds a 5$ feel will be deducted")
            self.balance[account] -= 5
            return self
        else:
            self.balance[account] -= amount
            return self

    def display_account_info(self):
        print(f"Balance = {self.balance}")
        return self

    def yield_interests(self):

        for i in self.balance:
            if self.balance[i] > 0:
                self.balance[i] = self.balance[i] + (self.balance[i] * self.int_rate)
            else:
                print(
                    f"The balance amount should not 0 or less / Current balance for {i}= {self.balance[i]}")
                return self
        return self


kareem = User("Kareem", "Kareem@outlook.com")
Zaid = User("Zaid", "Zaid@outlook.com")

kareem.account.deposit(100, "Account1").deposit(500, "Account2").withdraw(
    300, "Account2").yield_interests().display_account_info()
Zaid.account.deposit(200,"Account1").deposit(300,"Account1").withdraw(100,"Account1").withdraw(
    100,"Account1").withdraw(200,"Account1").yield_interests().display_account_info()
