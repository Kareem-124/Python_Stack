def big(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list


x = [1, 2, 3, 4, 5, 0, -4, -5]
x = big(x)
print(x)


# ------------ 2:
def count_positives(list):
    counter = 0
    for i in range(len(list)):
        if list[i] > 0:
            counter += 1
    list[len(list)-1] = counter
    return list


x = count_positives([-1, 1, -1, -1, 5, 4, 6, 5])
print(f"The Output of the 'count_positive' = {x}")


# ------------ 3:
def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum


x = sum_total([10, 10, 10, 10, 10, 10, -10, 0])
print(f"The Output of the 'sum_total' = {x}")

# ------------ 4:


def average(list):
    sum = 0
    avg = 0
    for i in range(len(list)):
        sum += list[i]
    avg = sum/len(list)
    return avg


x = average([10, 10, 10, 10, 10, 10, -10, 0, 10, 10])
print(f"The Output of the 'Average' = {x}")


# ------------ 5:

def length(list):
    return len(list)


x = [10, 10, 10, 10, 10, 10, -10, 0, 10, 10]
x = []
x = length(x)
print(f"The length of the array = {x}")


# ------------ 6:
def minimum(list):
    min = 0
    if len(list) == 0:
        return False
    for i in range(len(list)):
        if min > list[i]:
            min = list[i]
    return min


x = [-1, 1, -1, -1, 5, -44, 6, 5]
# x=[]
x = minimum(x)
print(f"The minimum value = {x}")


# ------------ 7:
def maximum(list):
    max = 0
    if len(list) == 0:
        return False
    for i in range(len(list)):
        if max < list[i]:
            max = list[i]
    return max


x = [-1, 1, -1, -1, 5, -44, 6, 55]
#x=[]
x = maximum(x)
print(f"The minimum value = {x}")


# ------------ 8:
def ultimate_analysis(list):
    max = maximum(list)
    min = minimum(list)
    avg = average(list)
    sum = sum_total(list)

    return {
        'sumTotal':sum,
        'average':avg,
        'minimum':min,
        'maximum':max,
        'length':length(list)
        }


x = [-1, 1, -1, -1, 5, -44, 6, 55]
#x=[]
x = ultimate_analysis(x)
print(f"The minimum value = {x}")


# ------------ 9:
def reverse_list(list):
    temp = 0
    for i in range(0,int(len(list)/2),1):
        temp = list[i]
        list[i]= list[len(list) - i -1]
        list[len(list)- i -1] = temp
    return list
x = [-1, 1, -1,5, -44, 6, 55]
x=reverse_list(x)
print(f"Reverse list = {x}")