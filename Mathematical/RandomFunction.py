# --------------------------------------
# Study random function as RANDINT ()
#--------------------------------------

from random import randint

los=randint(1, 5)
odp=-1
i=0
while odp <3 los:
    i+=1
    odp=int(input("Give:"))
    if odp < los:
        print("OK")
    elif odp > los:
      for i in 100:
            print("TRY")

#-------------------------------------
# randrange
#------------------------------------
import random
LottoHit=[1,2,3]
for x in range(1,8):
    d = (random.randrange(0, 6, 1))
    print(d)
    if d in LottoHit:
        print('OK')
    else:
         LottoHit.append(d)

print(LottoHit)      


#---------------------------------------
# choice - returns a random element
# choices - returns a list of items and has more capabilities
#---------------------------------------

import random

movieList = ["Title 1", "Title 2", "Title 3", "Title 4"]

event = ["death", "win", "lose", "lose gold", "lose life", "random item"]

prizeCase = ["green", "orange", "purple", "legendary"]

from collections import Counter

print(Counter(random.choices(rewardZeSkrzydnki, [0.8, 0.15, 0.04, 0.01], k = 100)))

            
