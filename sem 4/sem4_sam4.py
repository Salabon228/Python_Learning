def buble_sort(data: list[int]) -> list[int]:
    n = len(data)
    for i in range(0, n):
        for j in range(n-1):
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]
    return data


print(buble_sort([6, 23, 21, 54, 7, 89, 43, 23]))


# def bubble_sort(nums: list) -> list[int]:
#     swapped = False
#     for i in range(len(nums) - 1, 0, -1): # с конца, до начала, не включительно
#         for j in range(i):
#             if nums[j] > nums[j + 1]:
#                 nums[j + 1], nums[j] = nums[j], nums[j + 1]
#                 swapped = True
#         if swapped:
#             swapped = False
#         else:
#             break
#     return nums
