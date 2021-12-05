#-----------------------------
#Study 1
#Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie. ( Polish)
#Get three numbers from the user, check which one is the smallest and print it on the screen.
#----------------------------

# Solution
from pip._vendor.distlib.compat import raw_input
#print(f"wrote number:'a'= {a}, 'b'={b}, c={c}")
op = "t"
a = 0
b = 0
c = 0
arraYT = []
while op == "t":
    try:
     a, b, c = raw_input("Give three numbers separated by spaces: ").split(" ")
     end try :
     # - first solution
     arraYT= [a, b, c]
     print(f"numbers written out:a= {a}, b={b}, c={c}")
     print ("Enterned number:", a, b, c,)
     print   ("\the smallest: ",)
     print("Print array", arraYT)
     arraYT.sort()
     print(arraYT[0])

     if a < b:
         if a < c:
             print(a)
         else:
             print (c)
     elif b < c:
             print (b)
     else:
             print (c)

  



op = raw_input("One more time (t/n)? ")

print( "By, by...")
