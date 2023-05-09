# note you need to install colorama module before importing and using it here 
# 'pip install colorama'
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

import random
def randInt(min= 0  , max= 100  ):
    max = max - min
    num = round((random.random() * max) + min)
    return num

#Generate 50 values of each case to Validate it works preapply
for i in range(50):
    print(f"Using ranInt()                   : {randInt()}") 		                                            # should print a random integer between 0 to 100
    print(f"Using ranInt(max = 50)           : {Fore.YELLOW}{randInt(max=50)}{Style.RESET_ALL}") 	            # should print a random integer between 0 to 50
    print(f"Using ranInt(min = 50)           : {Fore.CYAN}{randInt(min=50)}{Style.RESET_ALL}") 	                # should print a random integer between 50 to 100
    print(f"Using ranInt(min = 50 max = 500) : {Fore.RED}{randInt(min=50, max=500)}{Style.RESET_ALL} \n")       # should print a random integer between 50 and 500

