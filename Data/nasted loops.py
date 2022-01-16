listaA=list(range(8))
listaB=list(range(8))

print( listaA, listaB)

product =[]

for a in listaA:
    for b in listaB:
        product.append((a,b))
print(product)


product =[(a,b) for a in listaA for b in listaA]
print(product)

product =[(a,b) for a in listaA for b in listaB if a%2==0  and b%2==0]
print(product)


# if we use dictionary
product ={a:b for a in listaA for b in listaB if a%2==1  and b%2==0}
print(product)




numbers = list(range(1, 10))

new_numbers = [x ** 2 for x in numbers]
print(new_numbers)