#----------------------------------------
# function raise and exception
#---------------------------------------

def divide (x,y):
    assert y !=0 "Y diffrent"
    if y==0:
      raise ZeroDivisionError
    print (x/y)
try:
    divide(2,0)
except  (ZeroDivisionError, TypeError):
    print("Error")
    raise
