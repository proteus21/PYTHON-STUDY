#-----------------------------------
# Even number calculation
#-----------------------------------

score =0
i = 0
while i < 3:
    x = int(input("Enter positive number"))
    if (x > 0 and x % 2 == 0 ):
        result += x
    else:
        print("There was supposed to be a positive number by 3 times")
        continue
    print("Current Score",score)
    # to turn off after 3 positives
    i+=1
