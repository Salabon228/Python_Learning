n = int(input("Введите число от 1 до 100 000: "))
res = []
if n > 1 and n < 100_000:
    while n > 1:
        for i in range(2, int(n * 0.5)+1):
            if n % i == 0:
                res.append(i)
        break
    if res != []:
        print("Это число составное, оно делится на: ", res)
    else:
        print('Число ', n, ' простое!')
else:
    print("Вы ввели число не из заданного диапазона")

