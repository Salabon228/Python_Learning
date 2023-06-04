def unicode_table(text: str) -> dict:
    num_1, num_2 = map(int, text.split())
    if num_2 < num_1:
        num_1, num_2 = num_2, num_1
    result = {}
    for num in range(num_1, num_2 + 1):
        result[chr(num)] = num
    return result


result = (unicode_table("66 99"))
print(result)
