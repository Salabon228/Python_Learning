import math
import decimal


decimal.getcontext().prec = 40
diameter = decimal.Decimal(input("Введите диаметр: "))

if diameter <= 0 or diameter > 1000:
    print("Неверный ввод данных")
else:
    square = decimal.Decimal(math.pi) * (diameter / 2) ** 2
    length_okr = 2 * decimal.Decimal(math.pi) * diameter / 2
print(f"{square = }, {length_okr = }")
