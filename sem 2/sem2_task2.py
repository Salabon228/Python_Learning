print('Вариант 1')
DATA = 'b', 'o', 'x'
num: int = int(input("Введите число "))
for char in DATA:
    print(format(num, char))
    # print(format(num, "o"))
print(f'Проверка: {bin(num) = }, {oct(num) = }')

print('Вариант 2')
ZERO = 0
BIN = 2
OCT = 8
n: int = int(input("Enter num: "))

for num in BIN, OCT, 9:
    work_num = n
    b: str = ""
    while work_num > ZERO:
        b = str(work_num % num) + b
        # b = y + b
        work_num = int(work_num / num) # n // BIN
    print(b)