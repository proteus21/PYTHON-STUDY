#--------------------------------------
# Study 2
#1,2,3,4 Liczby, liczby wzajemnie bez powtarzania liczb trzycyfrowych może składać? Ilu? (Polish)
#1,2,3,4 Numbers, mutual numbers without repeating three-digit numbers can assemble? How many? 
#--------------------------------------

# Solution

i=0
j=0
k=0
z=0

for i in range(5):
    for j in range(5):
        for k in range(5):
            #aby sie nie powtarzalo musi poszczegole liczby roznic sie od siebie ( ! )
            #to avoid repetition the numbers must be different from each other ( ! )
           if  ( i!=j) and (j!=k) and ( i!=k):
             z=z+1
           print( i, j, k)
print( "Variant number", z)
