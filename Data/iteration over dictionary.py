workDays = [19,21,22,21,20,22]
month= ["I","II","III","IV","V","VI"]

monthDays=dict(zip(month,workDays))
print(monthDays)

for key in monthDays:
    print("Key is", key, "value is", monthDays[key])

for value in monthDays.values():
    print(value)
    print('the value', value)
for value in monthDays.values():
    print(value)


    

instructions = {}

instructions['first name'] = 'john'
instructions['last name'] = 'walker'
instructions['street'] = 'Health and Strength street'
instructions['city'] = 'Moscow'

print(instructions.keys())