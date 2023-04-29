countDown_Value = 5


def countDown(val):
    list = []
    maxLimit = val + 1
    for i in range(0, maxLimit, 1):
        list.append(val)
        val -= 1
    return list


countList = countDown(countDown_Value)
print(f" The count down for {countDown_Value} is :{countList}")


def print_and_return(list):
    if len(list) == 2:
        print(f"the first value of print_and_return function ={list[0]}")
        return list[1]
    else:
        print("Please enter a list with only two values!")

# ----Second Function:


x = print_and_return([1, 2])
print(f"The value of returned value of the print_and return function = {x}")

# ----Third Function:


def first_plus_length(list):
    return list[0]+len(list)


x = first_plus_length([3, 2, 4, 5, 6, 4, 7])
print(f"The value of returned value of the first_plus_length function = {x}")

# ----Fourth Function:


def values_greater_than_second(list):
    if len(list) >= 2:
        counter = 0
        new_list = []
        for i in range(0,len(list),1):
            if list[i] > list[1]:
                counter += 1
                new_list.append(list[i])
        print(f"total value bigger than the second list value are ={counter}")
        return new_list
    else:
        return False

x = values_greater_than_second([3, 4, 4, 5, 6, 4, 7])
print(f"The value of returned value of the 'values_greater_than_second' function = {x}")

# ----Fifth Function:
def length_and_value(length,data):
    new_list=[]
    for i in range(0,length,1):
        new_list.append(data)
    return new_list

x= length_and_value(10,7)
print(f"The new list of 'length_and_value' function = {x}")
