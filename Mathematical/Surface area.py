#----------------------------------------
# Small programme to calculation surface area  for diffrent  mathematical fugures
#-------------------------------------------

from math import *
def rectangle(a,b):
    return a *b
def square (a):
    return a**2
def trinagle(a,h):
    return 0.5*a*h
def trapezoid(a, b, h):
    return (((a+b)/2)*h)
def circle(r):
    return pi*r**2
  
  from enum import IntEnum
IntEnum()
Menu_Figures = IntEnum('Menu_Figures', {'Square':1, 'Rectangle':2 , 'Circle':3, 'Triangle':4, 'Trapezoid':5})
print(list(Menu_Figures))
choice = int(input("""Select the figure whose area you want to calculate:
1. square
2. rectangle
3) Circle
4. triangle
5. trapezoid
"""))

while (True):
   print('------------------------------------------------------------------')
   print("Surface area calculation")
   print('------------------------------------------------------------------')
   print("1 - rectangle, 2 - square, 3 - triangle, 4 - trapezoid, 5 - circle :, 6- Finish")
   choose = int(input("Select area to calculate"))
   if (wybor == Menu_Figures):
     a = int(input("Give value a: "))
     b = int(input("Give value b: "))
     print("Rectangle area is =",rectangle(a,b))
   elif (choose == 2):
     a = int(input("Give value a "))
     print("Squere area is =", square(a))
   elif (choose == 3):
     a = int(input("Give value a "))
     h = int(input("Give value h (Height) "))
     print("Triagle area is =", trinagle(a, h))
   elif (choose == 4):
     a = int(input("Give value a "))
     b = int(input("Give value b "))
     h = int(input("Give value h (Height) "))
     print("Trapezoid area is =", trapezoid(a,b, h))
   elif (choose == 5):
    r = int(input("Give value r "))
    print("Circle area is =", circle(r))
   elif (choose ==6):
       print("Finish")
       break
   else:
        print("Given  over range")
