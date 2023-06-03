list_num = [1, 2, 3, 4, 6, 4, 9, 2, 3, 1, 5, 6, 9, 4, 2]
print(list_num)
res = []
for i, el in enumerate(list_num, start=1):
    if el % 2 != 0:
        res.append(i)
print(res)
