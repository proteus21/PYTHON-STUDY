#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


from pip._vendor.distlib.compat import raw_input
n =int(raw_input('Give the range,'))
d=dict()
i=1
for i in range(n):
   d[i]=i*i

print (d)
