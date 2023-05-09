class user:
    def __init__(self,name):
        self.name=name
        self.balance =0
    def depose(self,amount):
        self.balance+=amount
    def make_withdrawal(self, amount):
        self.balance-=amount
    def display_user_balance(self):
        print(f"The User {self.name} has a balance of {self.balance} $")
    def transfer_money(self, other_user, amount):
        self.balance-=amount
        other_user.depose(amount)

kareem=user("Kareem")
ahmed=user("Ahmed")
samer=user("Samer")

print(kareem.name)
kareem.depose(500)
kareem.depose(200)
kareem.depose(300)
kareem.make_withdrawal(200)
kareem.display_user_balance()

ahmed.depose(1500)
ahmed.depose(700)
ahmed.make_withdrawal(500)
ahmed.make_withdrawal(800)
ahmed.display_user_balance()

samer.depose(5000)
samer.make_withdrawal(1000)
samer.make_withdrawal(500)
samer.display_user_balance()

kareem.transfer_money(ahmed,500)
kareem.display_user_balance()
ahmed.display_user_balance()
