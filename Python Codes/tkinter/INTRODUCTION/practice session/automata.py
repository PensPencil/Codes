# import everything from sympy module
from sympy import * x = Symbol('x')
y = Symbol('y')

z = (x + y) + (x-y)
print("value of z is :" + str(z))
