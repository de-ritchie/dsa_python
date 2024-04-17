"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

def two_sum(nums, target, i, j, init, res):

    while i < j:

        tmp_sum = nums[i] + nums[j]

        if tmp_sum == target:
            res.append([init, nums[i], nums[j]])
            i += 1
            j -= 1

            # Remove duplicate elements
            while nums[j] == nums[j + 1] and i < j:
                j -= 1
        elif tmp_sum < target:
            i += 1
        else:
            j -= 1

def three_sum(nums, target):

    nums = sorted(nums)
    res = []
    size = len(nums)

    for i in range(size):
        
        if i + 2 >= size:
            break
        
        # Remove duplicate elements
        if i > 0 and nums[i] == nums[i-1]:
            continue

        num = nums[i]
        two_sum(nums, target - num, i + 1, size - 1, num, res)
    
    return res

print(three_sum([-1,0,1,2,-1,-4], 0))