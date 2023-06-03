data = input("Введите что-то: ")
data = sorted(data.split())
# res = data.split(' ')
# res = sorted(res)
# print(res)
max = 0

for i in data:
    if len(i) > max:
        max = len(i)
print(max)

for i, el in enumerate(data, start=1):
    print(f'{i} {el:>{max}}')