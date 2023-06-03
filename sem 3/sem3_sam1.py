data = [1, 2, 3, 4, 5, 222, 6, 7, 8, 1, 2, 3, 4, 5, 6,
        7, 8, 5, 3, 2, 1, 11, 3, 4, 6, 87, 4, 3, 23, 5]
res = []
for i in data:
    if i in res:
        a = 1
    else:
        res.append(i)


print(res)
