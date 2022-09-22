from sympy import *

def f(x):
    return x ** 2

a = -10
b = 10
#------------------SIMPLE-------------------
h = 1000
step = (b - a) / h
temp = a
min = f(a)
while (temp < b):
    value = f(temp)
    if (value < min):
        min = value
    temp += step
print(min)
#-------------------------------------------
#----------------DICHOTOMY------------------
h = 0.001
temp_a = a
temp_b = b
while (temp_b - temp_a > h):
    temp_c = (temp_a + temp_b) / 2
    if (f(temp_b) * f(temp_c) <= 0):
        temp_a = temp_c
    else:
        temp_b = temp_c
answer = (temp_a + temp_b) / 2
print(answer)
#-------------------------------------------
#------------------GOLDEN-------------------
h = 0.001
temp_a = a
temp_b = b
golden = (1 + 5 ** 0.5) / 2
while (abs(temp_b - temp_a) > h):
    x1 = temp_b - (temp_b - temp_a) / golden
    x2 = temp_a + (temp_b - temp_a) / golden

    if (f(x1) > f(x2)):
        temp_a = x1
    else:
        temp_b = x2
        
answer = (temp_a + temp_b) / 2
print(answer)
#-------------------------------------------