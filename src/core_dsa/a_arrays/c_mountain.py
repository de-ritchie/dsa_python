"""
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
"""

def longest_mountain(arr):

    start = 1
    end = len(arr) - 2
    max_count = 0
    i = start

    while i <= end:
        
        if arr[i-1] >= arr[i] or arr[i] <= arr[i+1]:
            i += 1
            continue

        cnt = 1
        j = i
        
        while j >= start and arr[j] > arr[j-1]:
            cnt += 1
            j -= 1
        
        while i <= end and arr[i] > arr[i+1]:
            cnt += 1
            i += 1
        
        max_count = max(cnt, max_count)
        
        i += 1
    
    return max_count

print(longest_mountain([2,1,4,7,3,2,5]))
print(longest_mountain([2,2,2]))
print(longest_mountain([0,1,0]))