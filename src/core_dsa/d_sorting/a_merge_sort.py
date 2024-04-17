"""
Merge Sort
"""

def merge_sort(nums, start, end):

    # Base condition
    if start == end:
        return [nums[start]]

    m = (start + end)//2

    # Divide
    left = merge_sort(nums, start, m)
    right = merge_sort(nums, m+1, end)

    # merge
    merge = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1
    
    while i < len(left):
        merge.append(left[i])
        i += 1
    
    while j < len(right):
        merge.append(right[j])
        j += 1

    return merge

def sort(nums):
    return merge_sort(nums, 0, len(nums) - 1)


print(sort([5,2,3,1]))
print(sort([5,1,1,2,0,0]))