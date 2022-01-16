var_x=10
password='My secret password'
source="password"

globals=globals().copy()
del globals ['password']
globals ={}

result=eval(source, globals)
print( result)
