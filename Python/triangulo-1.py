from math import sqrt

def area_triangulo(a,b,c):
    s = a + b + c
    return sqrt(s * (s - a) * (s - b) * (s - c))

s = 4
print(area_triangulo(s-1, s, s+1))
print(s)
print(a)