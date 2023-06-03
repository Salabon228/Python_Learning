items = [
    {'name': 'Sleeping Bag', 'weight': 4},
    {'name': 'Tent', 'weight': 7},
    {'name': 'Water Bottle', 'weight': 2},
    {'name': 'Food', 'weight': 5},
]

data = {
    'палатка': 5,
    'еда': 5,
    'сковорода': 1,
    'спальник': 1,
    'фонарик': 0.5,
    'топор': 2,
    'аптечка': 0.5,
    'вода': 0.5,
}

weight_limit = 2

combinations = [[]]  # Изначально имеем только пустую комбинацию

for k,v in data.items():
    new_combinations = []

    for combination in combinations:
        new_combination = combination + [k]

        # Проверяем, не превышает ли общий вес комбинации грузоподъемность
        total_weight = sum(v for k in new_combination)
        if total_weight <= weight_limit:
            new_combinations.append(new_combination)
        
    combinations += new_combinations

for combination in combinations:
    print(combination)