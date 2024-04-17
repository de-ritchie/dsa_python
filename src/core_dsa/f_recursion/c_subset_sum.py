"""
Subset Sum

Example 1:

Input: arr = [1, 2, 3, 4, 5] k = 6
Output: 6
"""

def subset_sum(nums, k, curr, i):
    
    if len(nums) == i:
        if curr == k:
            return 1
        return 0

    c = 0
    c += subset_sum(nums, k, curr + nums[i], i + 1)
    c += subset_sum(nums, k, curr, i + 1)

    return c


print(subset_sum([1, 2, 3, 4, 5], 6, 0, 0))
print(subset_sum([1, 1, 4, 5], 5, 0, 0))