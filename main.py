def twoSum(self, nums: list[int], target: int) -> list[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indexes = {}  # словарь для хранения значений и соответствующих им индексов
    for i in range(len(nums)):
        complement = target_sum - nums[i]
        if complement in indexes:
            return [indexes[complement], i]
        else:
            indexes[nums[i]] = i
    return None

# Пример использования
my_list = [1, 2, 3, 4, 5, 6]
target_sum = 9
result = twoSum(my_list, target_sum=9)
if result:
    print(f"Индексы элементов сумма которых равна {target_sum}: {result}")
else:
    print(f"Пара элементов сумма которых равна {target_sum} не найдена.")
