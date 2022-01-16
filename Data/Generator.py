listaA=list(range(8))
listaB=list(range(8))

print( listaA, listaB)

product =[]



gen =((a,b) for a in listaA for b in listaB if a%2==0  and b%2==0)
print(gen)
print(next(gen))

while True:
    try:
        print(next(gen))
    except StopIteration:
        print('All values was showed')
        break
