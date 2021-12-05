"""
    dictionary expression
"""

names = { "Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = { 't1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

giveName ={
    name: len(name)
    for name in names
    if name.startswith("A")
}
print(giveName)

print("Raises to power")
power ={
 number: number ** 2
      for number in numbers
 }
print(power)

multipleNumbers ={
        number: number ** number
    for number in range (0, 100)
}
print(multipleNumbers)

print(" Converter temperature")

farenheitT ={
          key: celcius * 1.2+32
          for key,celcius in celcius.items()
    if celcius > -5
}
print(farenheitT)

farenheitT1 ={
          key: celcius **2
          for key,celcius in celcius.items()
    if celcius > -5
}
print(farenheitT1)
