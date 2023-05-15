class base:
    def __init__(self):
        self.a = 2


class something(base):
    def __init__(self):
        
        base.__init__(self)
        print(f"Hello I will change the variable now")
        self.__a = 5

x=base()
y=something()
print(f"The value of a = {y.__a}")

