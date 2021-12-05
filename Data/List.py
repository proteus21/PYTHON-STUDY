#-----------------------------------
# Two way to write lists out
#-----------------------------------
numbers = [1, 2, 3, 4, 5, 6]

print(Old way to write list")
potegiDwojki = []
for element in numbers:
    potegiDwojki.append(element ** 2)
print(potegiDwojki)

print("New way to write list")
potegaDwojki2 = [element ** 2
                for element in liczby
                 ]
print(potegaDwojki2)

print("For even numbers ")

liczbaParzysta = [element
                for element in numbers
                if ( element %2 ==0)
                  ]
print(liczbaParzysta)
