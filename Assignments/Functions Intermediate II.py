from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# -- Task 1: Update Values in Dictionaries and Lists
print(f"\n \n {Fore.YELLOW}>>Task 1: Update Values in Dictionaries and Lists {Style.RESET_ALL} ")

def update():
    x[1][0] = 15                            #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    students[0]["last_name"] = "Bryant"     #Change the last_name of the first student from 'Jordan' to 'Bryant'
    sports_directory["soccer"][0]= "Andres" #In the sports_directory, change 'Messi' to 'Andres'
    z[0]["y"] = 30                          #Change the value 20 in z to 30


update()

#-- Task 2:Iterate Through a List of Dictionaries
print(f"\n \n {Fore.YELLOW}>>Task 2:Iterate Through a List of Dictionaries {Style.RESET_ALL} ")
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in students:
        print(f"first_name {Fore.RED}-{Style.RESET_ALL} {i['first_name']} , last_name {Fore.RED}-{Style.RESET_ALL} {i['last_name']} ")

iterateDictionary(students)

#-- Task 3: Get Values From a List of Dictionaries
print(f"\n \n {Fore.YELLOW}>>Task 3: Get Values From a List of Dictionaries {Style.RESET_ALL} ")
def iterateDictionary2(key_name, some_list):
    print(f"The value of {key_name} from the list =")
    for i in some_list:
        print(f"{i[key_name]}")

iterateDictionary2("last_name",students)


#-- Task 3.1: Get Values From a List of Dictionaries
print(f"\n \n {Fore.YELLOW}>>Task 3: Get Values From a List of Dictionaries {Style.RESET_ALL} ")
def iterateDictionary2(key_name, some_list):
    print(f"The value of {key_name} from the list =")
    for i in range(0,len(some_list),1):
        print(f"{some_list[i][key_name]}")

iterateDictionary2("last_name",students)

#-- Task 4: Iterate Through a Dictionary with List Values
print(f"\n \n {Fore.YELLOW} >>Task 4: Iterate Through a Dictionary with List Values {Style.RESET_ALL} ")

def printInfo(some_dict):
    for i in some_dict:
        print(f"{Fore.CYAN}{len(some_dict[i])}{Style.RESET_ALL} {i} ")
        for j in some_dict[i]:
            print(f"{j}")


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)




#copy and paste to test:
    #print(f"the value of x[1][0] = {x[1][0]}")
    #print(f"the value of x = {x}")
    #print(f"the value of students['last_name'] = {students[0]['last_name']}")
    #print(f"The value of sports['soccer'][0] = {sports_directory['soccer'][0]}")
    #print(f"The value of Z[0]['y']= {z[0]['y']}")