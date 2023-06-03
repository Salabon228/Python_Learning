list_num = [1, 2, 3, 4, 6, 4, 9, 2, 3, 1, 5, 6, 9, 4, 2]
print(list_num)

for i, el in enumerate(list_num, start=0):
    if list_num.count(el) == 2:
        while list_num.count(el):
            list_num.remove(el)
print(list_num)