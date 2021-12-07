#-------------------------------------
# Find numbers from 2 to 470 inclusive that are:
#  divisible by 7, but are not divisible by 5

# What will you use?
# 1) a generator
# 2) a list expression
# 3) set expression
# 4) a dictionary expression

# Consider, is the answer to this question always the same?
# range(100, 471)
# 7 14 21 28 35 ... 5 10 15 20 25 30 35 ---
# 7 % 7 == 0
# 14 % 7 == 0
# 21 % 7 == 0
# 35 % 5 == 0
# 7 % 5 == 2
# 14 % 5 == 4
#-----------------------------------

numbers = {
    number
    for number in range(2, 471)
    if (number % 7 == 0)
    if (number % 5 != 0)
}

print(numbers)
