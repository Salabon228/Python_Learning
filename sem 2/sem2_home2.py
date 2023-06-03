def add_fractions(fraction1, fraction2):
    # Разделяем числитель и знаменатель для первой дроби
    a1, b1 = fraction1.split('/')
    a1, b1 = int(a1), int(b1)

    # Разделяем числитель и знаменатель для второй дроби
    a2, b2 = fraction2.split('/')
    a2, b2 = int(a2), int(b2)

    # Находим общее знаменатель
    lcm = b1 * b2
    a1 *= b2
    a2 *= b1

    # Складываем дроби
    a_sum = a1 + a2

    # Сокращаем дробь
    gcd = find_gcd(a_sum, lcm)
    a_sum //= gcd
    lcm //= gcd

    # Возвращаем результат в виде строки
    return str(a_sum) + '/' + str(lcm)


def find_gcd(a, b):
    while a:
        b, a = a, b % a
    return b


fraction1 = '2/3'
fraction2 = '1/5'

result = add_fractions(fraction1, fraction2)
print(result)  # выводит '5/4'