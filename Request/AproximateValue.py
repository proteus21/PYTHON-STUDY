#-------------------------
# Give value and find
#-----------------------
print ('Aproximate Value')
def findAproximateValue(value):
    lovestValue = value -0.1 * value
    highestValue = value + 0.1 * value
    return(lovestValue, highestValue )

print( findAproximateValue(100))
