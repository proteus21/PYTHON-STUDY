#Question:
#Write a program which will find all such numbers which are divisible by 9 but are not a multiple of 8,
#between 1000 and 5200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

l=[]
for i in range(1000, 5201):
    if (i%9==0) and (i%8!=0):
        l.append(str(i))

print(l)
