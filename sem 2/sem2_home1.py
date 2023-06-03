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
HEX = 16
n: int = int(input("Enter num: "))
check_16 = {'10': 'А', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
for num in OCT, HEX:
    work_num = n
    b: str = ""
   
    while work_num > ZERO:
        ost = work_num % num
        if num == HEX and (9 < ost < num):
            b = str(check_16[str(ost)]) + b
        else:
            b = str(ost) + b
        work_num = int(work_num / num) # n // BIN
    
        
    print(b)