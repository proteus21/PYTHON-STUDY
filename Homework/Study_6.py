#-------------------------------------------------------------
# Create a function that generates infinitely consecutive numbers multiplied by itself ie:
# 1 4  9  16 25 36
# Use the generating function to generate 20 elements, then go back from the end and generate 30 more numbers after that.
# Save the generated elements in the same list.
#--------------------------------------------------------------

def number_multiplied_by_itself_generator():
    number = 0
    while True:
        number = number + 1
        yield number * number

generatedNumbers = []

numberGenerator = number_multiplied_by_itself_generator()

for _ in range(20):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)

for _ in range(30):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)    
