#---------------------------
# Mathematical function
#-------------------------

import math

def sum (x):
    return (x)+1
    variable=sum
print(variable(4))

def calc(x,y):
    return x+y/2
    variableCal=cal
print(variableCal(4,5))

def silnia (x):
    if x<=1:
        return 1
    else:
         return x* silnia(x-1)


print(silnia(1))
