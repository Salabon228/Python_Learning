def get_dict(**kwargs) -> dict:
    res = {}
    for key, value in kwargs.items():
        value_str = str(value)
        res.setdefault(value_str, key)
        # print(res)
    return res

result = get_dict(name='das', value=(2,2))
print(result)