"""
Inversion Count

Input: [2, 4, 1]
Output: 2
Explanation: (4, 1), (2, 1)
"""

def merge_sort(nums, start, end):

    # Base condition
    if start == end:
        return ([nums[start]], 0)

    m = (start + end)//2

    # Divide
    left, c1 = merge_sort(nums, start, m)
    right, c2 = merge_sort(nums, m+1, end)

    # merge
    merge = []
    i = 0
    j = 0
    c = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
            # print('-----', m, i)
            c += len(left) - i
    
    while i < len(left):
        merge.append(left[i])
        i += 1
    
    while j < len(right):
        merge.append(right[j])
        j += 1

    # print(c1, c2, c, merge)
    return (merge, c1 + c2 + c)

def sort(nums):
    return merge_sort(nums, 0, len(nums) - 1)[1]

print(sort([2, 4, 1]))
print(sort([1, 1, 1, 2, 2]))
print(sort([7, 5, 3, 1])) # (7, 5), (7, 3), (7, 1), (5, 3), (5, 1), (3, 1)