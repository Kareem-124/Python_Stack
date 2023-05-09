class user:
    def __init__(self,name,email_address):
        self.name=name
        self.email=email_address
        self.account_balance = 0
        self.sum=0
    def add(self, numb1,numb2):
        self.sum = 0
        self.sum= numb1 + numb2
        

Zain = user("zain","Zain@outlook.com")
#Kareem= user()
Zain.add(5,10)
print(Zain.sum)
#print(Kareem.name)




