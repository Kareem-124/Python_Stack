for i in range(151):
    print(i)
num=5
for i in range(5,1001,5):
    print(i)
for i in range(1,101,1):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)
sum = 0
for i in range(500001):
    if i%2 !=0:
        sum +=i
print(f"The total sum of Odd numbers = {sum}")

for i in range(2018,0,-4):
    print(i)

lowNum=2
highNum=10
mult=2

for i in range(lowNum,highNum+1,1):
    if mult == 0:
        print("Please enter a multi value bigger than 0!")
        break
    elif i%mult == 0:
        print(i)
