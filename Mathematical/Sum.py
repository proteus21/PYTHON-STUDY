valueS = (2,4,1,2,4,5,10)

print("step 1")

def suma1(value):
    suma=0
    for i in value:
        suma=suma+i
    return suma
print(suma1(valueS))

print("step 2")

def suma2(value):
     return sum( i  for i in value)

print(suma2(valueS))

def suma3(value):
    return ({ i  for i in value })
 # slownik nie powtarza liczb
print(suma3(valueS))

def suma4(value):
    return sum([ i  for i in value ])

print(suma4(valueS))
