#1
def a():
    return 5
print(a())
print("My prediction is : 5")
#2
def a():
    return 5
print(a()+a())
print("My prediction is : 10")
#3
def a():
    return 5
    return 10
print(a())
print("My prediction is : 5")
#4
def a():
    return 5
    print(10)
print(a())
print("My prediction is : 5")
#5
def a():
    print(5)
x = a()
print(x)
print("My prediction it will print 5 twice")
#6
def a(b,c):
    print(b+c)
#print(a(1,2) + a(2,3))
print("My prediction it will print 8... wrong it printed 3 then 5 but then gave an error if we put a return b+c it will work and then print 8")
#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
print("My prediction it will print 25 as a string")
#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    
    else:
        return 10
    return 7

print(a())
print("My prediction it will print 100 then 10")
#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # it will print 7
print(a(5,3)) # it will print 14
print(a(2,3) + a(5,3)) # it will print 21
print("My prediction it will print 7,14 and 21")
#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
print("My prediction it will print 8")
#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
print("My prediction it will print 500, 500, 300, and 300.... wrong it printed 500,500,300 and 500 my guess that the variable b inside the function is a local variable (inside the function scope only) and dose not effect the global variable b")
#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
print("My prediction it will print 500, 500, 300, and 500")
#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
print("My prediction it will print 500, 500, 300, and 300")
#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
print("My prediction it will print 1, 3, and 2")
#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
print("My prediction it will print 1,3,5 and 10")























