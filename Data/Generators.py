#-------------------------------
# Generators
#--------------------------------
import sys

evenNumbers = [element
               for element in range(400)
               if (element % 2 == 0)
               ]

evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0)
                        )
print(sum(evenNumbersGenerator))
print(sum(evenNumbers))
print(sys.getsizeof(evenNumbersGenerator))
