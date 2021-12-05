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
