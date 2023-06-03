import sys


data = [ 2345, 3.1415, 'qwert']
for num, item in enumerate(data, start=1):
    print(f"{num}    {item}, {id(item)=}, {sys.getsizeof(item)=}, {hash(item)=}")
    check_int = "Объект целый" if isinstance(item, int) else ''
    check_str = "Объект строка" if isinstance(item, str) else ''
    print(check_int, check_str)
    print('*' * 50)