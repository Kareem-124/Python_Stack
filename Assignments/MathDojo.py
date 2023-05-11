'''
This is a  mathematical class which create objects that mainly make two operations:
1- Addition
2- Subtract
*- Any operation needs at least 1 input (argument) 

Available methods are :
.add()        --> Additive Operation
.subtract()   --> Subtract Operation
.restuls()    --> Print the Result on Terminal

'''


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        if len(nums) > 0:
            for i in nums:
                self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        if len(nums) > 0:
            for i in nums:
                self.result -= i
        return self

    def results(self):
        print(f"Result = {self.result}")
        return self


# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(8).add(10, 20).subtract(10).subtract(10, 10, 10).result
md.results()


print(x)
