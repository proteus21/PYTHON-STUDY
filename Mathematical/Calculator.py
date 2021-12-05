#---------------------------
# Simple calculator
#---------------------------

print("Calculator")
choice = input( " * - multiplication, / - division, + - addition, ^- conjunction")
a = int(input("First number a="))
b = int(input("Second number b="))
if (choice == "*"):
    print(a*b)
elif (choice == "/"):
    if (b == 0):
        print("You are dividing by zero")
    else:
        print(a / b)
elif (choice == "+"):
    print (a+b)
elif (choice == "^"):
    print(a**b)
else:
    print("You did nothing")
