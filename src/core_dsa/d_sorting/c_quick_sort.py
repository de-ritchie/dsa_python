"""
Quick Sort
"""

import random

def quick_sort(nums, start, end):

    # Base condition
    if start >= end:
        return nums

    pivot_idx = end
    pivot = nums[pivot_idx]
    i = start - 1

    # Partition
    for j in range(start, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    i += 1
    nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
    
    quick_sort(nums, start, i - 1)
    quick_sort(nums, i + 1, end)

    return nums

def quick_sort_alt(nums):

    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)

    left = []
    equal = []
    right = []

    for num in nums:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    return quick_sort_alt(left) + equal + quick_sort_alt(right)

def sort(nums):
    # return quick_sort(nums, 0, len(nums) - 1)
    return quick_sort_alt(nums)


print(sort([5,2,3,1]))
print(sort([5,1,1,2,0,0]))