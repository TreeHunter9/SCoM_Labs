from sympy import *

#-----------------DIFF----------------
def f(x):
    return x ** 2

x = Symbol('x')
deltaX = 0.001
f_diff = diff(x ** 2, x)
result = f_diff.subs(x, 2)
result_n = (f(2 + deltaX) - f(2)) / deltaX
print(result, result_n)
#--------------------------------------
#---------------INTEGRAL---------------
x = Symbol('x')
a = 4
b = 8
h = 10
result = integrate(x ** 2, (x, a, b))
result_n = 0.0
step = (b - a) / h
while(a < b):
    result_n += step * f(a)
    a += step

print(result, result_n)
#--------------------------------------