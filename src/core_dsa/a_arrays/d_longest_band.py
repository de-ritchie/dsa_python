"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""

def longest_consecutive(nums):

    if len(nums) == 0:
        return 0
    # nums = list(set(nums))
    nums = sorted(nums)
    print(nums)
    max_cnt = 1
    cnt = 1

    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            continue
        if nums[i] + 1 == nums[i+1]:
            cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
            cnt = 1
    return max(cnt, max_cnt)

def longest_consecutive_alt(nums):

    if len(nums) == 0:
        return 0
    
    nums_set = set(nums)
    accu_set = set()
    max_cnt = 1

    for num in nums_set:
        
        if num in accu_set:
            continue
        
        num_ = num
        cnt = 1
        while num_ - 1 in nums_set:
            num_ -= 1
            accu_set.add(num_)
            cnt += 1

        while num + 1 in nums_set:
            num += 1
            accu_set.add(num)
            cnt += 1
        
        max_cnt = max(cnt, max_cnt)
    
    return max_cnt
        


print(longest_consecutive([100,4,200,1,3,2]))
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))
print(longest_consecutive([1,2,0,1]))

print(longest_consecutive_alt([100,4,200,1,3,2]))
print(longest_consecutive_alt([0,3,7,2,5,8,4,6,0,1]))
print(longest_consecutive_alt([1,2,0,1]))