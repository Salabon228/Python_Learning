random_tuple = (1, 2.13, 5, 8.12, 'hello', 8, 'hi', True, [1, 2, 3], [4, 5, 6], None)
result = {}
values = []
for item in random_tuple:
    values = result.get(type(item))
    if values:
        values.append(item)
    else:
        values = [item]
    result.setdefault(type(item), values)
print(result)

print('*' * 50)
d = {}

for i in random_tuple:
    d.setdefault(type(i), []).append(i)
print(d)

print('*' * 50)
result_dict = {}

for item in random_tuple:
    item_type = type(item)
    if item_type in result_dict:
        result_dict[item_type] += [item]
    else:
        result_dict[item_type] = [item]

print(result_dict)