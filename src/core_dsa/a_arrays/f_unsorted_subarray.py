"""
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, 
then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:

Input: nums = [1,2,3,4]
Output: 0

Example 3:

Input: nums = [1]
Output: 0
"""

def is_swap_req(nums, i, size):

    if i == 0:
        return nums[i] > nums[i+1]
    if i == size - 1:
        return nums[i-1] > nums[i]
    return nums[i-1] > nums[i] or nums[i] > nums[i+1]

def find_unsorted_subarray(nums):

    small = float('inf')
    large = float('-inf')
    size = len(nums)

    if size == 0 or size == 1:
        return 0

    for i in range(size):
        
        if is_swap_req(nums, i, size):
            small = min(nums[i], small)
            large = max(nums[i], large)

    if small == float('inf') or large == float('-inf'):
        return 0
    
    # Forward Pass
    for i, num in enumerate(nums):
        if num > small:
            break

    # Backward Pass
    for j in range(size-1, -1, -1):
        num = nums[j]
        if num < large:
            break
    
    return j - i + 1
    

print(find_unsorted_subarray([2,6,4,8,10,9,15]))
print(find_unsorted_subarray([1,2,3,4]))
print(find_unsorted_subarray([1]))
print(find_unsorted_subarray([2, 1]))