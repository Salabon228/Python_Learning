from random import randint
num = randint(0, 1000)
count = 10
# print("num = ", num)
while count > 0:
    count -= 1
    user_num = int(input("Введи число: "))
    if user_num == num:
        print("ВЫ УГАДАЛИ! это было число ", num)
        break
    elif user_num < num:
        print("Загаданное число больше вашего")
    else:
        print("Загаданное число меньше вашего")
    print("У вас осталось ", count, " попыток")
else:
    print("ВЫ НЕУГАДАЛИ ЧИСЛО", num)