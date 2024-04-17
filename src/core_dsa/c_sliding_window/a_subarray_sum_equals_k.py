"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""

def sub_array_sum(nums, k):

    mapper = {}
    mapper[0] = 1
    c = 0
    s = 0

    for i, num in enumerate(nums):
        s += num
        check = mapper.get(s - k, None)
        if check is not None:
            c += mapper.get(s - k)
        mapper[s] = mapper.get(s, 0) + 1
    
    return c

print(sub_array_sum([1,1,1], 2))
print(sub_array_sum([1,2,3], 3))
print(sub_array_sum([1], 0))
print(sub_array_sum([-1,-1,1], 0))
print(sub_array_sum([1,-1,0], 0))
print(sub_array_sum([0,0,0,0,0,0,0,0,0,0], 0))