"""
Sqrt(X)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

def sqrt(x):
    
    start = 0
    end = x
    res = None

    while start <= end:
        
        mid = (start + end)//2
        square = mid * mid
        
        if square == x:
            return mid
        elif square <= x:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return res

print(sqrt(8))
print(sqrt(9))
print(sqrt(16))
print(sqrt(26))