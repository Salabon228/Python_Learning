int_list = [1,3,6,2,4,7,6,2,5,7,8]



print(list(set(int_list)))



list_from_cycle = []
for num in int_list:
    if num not in list_from_cycle:
        list_from_cycle.append(num)
print(f"{list_from_cycle = }")