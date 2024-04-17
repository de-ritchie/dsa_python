"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

def construct_max_array(nums):
    res = [nums[0]]
    for i in range(1, len(nums)):
        num = nums[i]
        res.append(max(num, res[-1]))
    return res

def trap(height):

    left = construct_max_array(height)
    right = construct_max_array(height[-1::-1])[-1::-1]
    res = 0

    for h, l, r in zip(height, left, right):
        res += min(l, r) - h
    
    return res

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))