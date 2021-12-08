#--------------------------
# Generator and yield function
#------------------------------------

def generator():
    number=0
    while (True):
        number+=1
        yield number*number
generatedNumber =[]
numberGenerator = generator()

for _ in range(20):
  generatedNumber.append(next(numberGenerator))

print(generatedNumber)

for _ in range(30):
  generatedNumber.append(next(numberGenerator))

print(generatedNumber)


