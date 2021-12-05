mylist = [(3, 5, 8), (6, 2, 8), ( 2, 9, 4), (6, 8, 5)]
t = sorted(mylist, key=lambda x:(x[0],x[1]))
print(t)

# Working list [array]
print('tupla  and  multicolum array')
# Tupla
tupla=[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')] # tupla zamykana jest w ()
t1 = sorted(tupla, key=lambda x:(x[0],x[1]))
print(t1)

# sort the
from operator import itemgetter, attrgetter
print('tupla  and  itemgetter, attrgetter')
print(sorted(tupla, key=itemgetter(0,1,2)))


# list
print('Lista')
nums = ["2", 1, 3, 4, "5", "8", "-1", "-10"]
print(sorted(nums, key=int))

li = [["user1", 100], ["user2", 234], ["user3", 131]]

import operator

print(sorted(li, key=operator.itemgetter(1)))   # Ascending order
#[['user1', 100], ['user3', 131], ['user2', 234]]

print(sorted(li, key=operator.itemgetter(1), reverse=True))  # Reverse Sort
#[['user2', 234], ['user3', 131], ['user1', 100]]
