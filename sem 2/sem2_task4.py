import cmath
ur = 'a * x ** 2 + b * x + c = 0'

a = 0
b = 5
c = -10

if a == 0:
    print("Это не квадратное уравнение")
    x = -c / b
    print(f"{x = }")
    exit()
d = b ** 2 - 4 * a * c
print(f"{d = }")
x1 = (-b + cmath.sqrt(d)) / (2 * a)
print(f"{x1 = }")
x2 = (-b - cmath.sqrt(d)) / (2 * a)
print(f"{x2 = }")
