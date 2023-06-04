def list_sum_2(numbers: list, start_idx: int, end_idx: int):
    i = min(start_idx, end_idx) if min(start_idx, end_idx) >= 0 else 0
    j = max(start_idx, end_idx) if max(start_idx, end_idx) < len(numbers) else len(numbers)
    return sum(numbers[i:j])


res = list_sum_2([1, 2, 3, 4, 5], 2, 22)
print(res)
print(f'{sum([]) = }')
