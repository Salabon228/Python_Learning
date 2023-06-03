data = input("Введите данные: ")

if data.isdigit() and int(data) > 0:
    print("Это целое положительное число")
elif data.isalpha():
    if data.lower() == data:
        print('В нижнем регистре')
    else:
        print('Верхний регистр')
elif data.count('-') <= 1 and data[1:].count('-') == 0 and data.count('.') == 1 \
    and data.replace('-', '').replace('.', '').isdigit():
    print('Вещественное ')