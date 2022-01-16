workDays = [19,21,22,21,20,22]

enumaratedDays = list(enumerate(workDays))
print(enumaratedDays)

for number, value in enumaratedDays:
    print("Position:",number,"value:", value)

month= ["I","II","III","IV","V","VI"]

monthDays =list(zip(month, workDays))

for m, d in monthDays:
    print("Month:",m,"Days:", d)

for number,(m,d) in list(enumerate(monthDays)):
    print("Position", number, "Month:",m,"Days:", d)
