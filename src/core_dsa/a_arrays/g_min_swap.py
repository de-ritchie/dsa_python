"""
Example 1:

Input: nums = [5,4,3,2,1]
Output: 
"""

def min_swap(nums):

    nums_idx = [(idx, num) for idx, num in enumerate(nums)]
    nums_sorted = sorted(nums_idx, key=lambda x: x[1])
    visited = [0 for _ in nums]
    swaps = 0

    for idx, (num_idx, num) in enumerate(nums_sorted):
        
        if visited[idx] == 1 or idx == num_idx:
            visited[idx] = 1
            continue
        
        # swap
        while idx != num_idx and visited[idx] == 0 and visited[num_idx] == 0:
            swaps += 1
            nums_sorted[idx], nums_sorted[num_idx] = nums_sorted[num_idx], nums_sorted[idx]
            visited[num_idx] = 1
            num_idx = nums_sorted[idx][0]
        
        visited[idx] = 1
    
    print(nums_sorted)

    return swaps

print(min_swap([5,4,3,2,1]))
print(min_swap([5,4,1,2,3]))