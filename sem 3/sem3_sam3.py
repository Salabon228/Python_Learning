
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

load_beariing = float(input("Введите грузоподъемность рюкзака: "))
my_items = 0
my_items_list = []
for k,v in data.items():
    if my_items <= load_beariing:
        if my_items+v <= load_beariing:
            print(f"Мы можем {k} весом {v}")
            my_items += v
            my_items_list.append(k)
            print(f"Общая загрузка станет {my_items}")
        else:
            continue
print(f"Мы можем взять с собой: {my_items_list}")