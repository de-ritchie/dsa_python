"""
No. of ways to reach a ladder

Example 1:
Input: 4
Output: 7
"""

def ladder_recurs(n):

    if n == 0:
        return 1
    
    c = 0

    if n >= 3:
        c += ladder_recurs(n-3)
    if n >= 2:
        c += ladder_recurs(n-2)
    if n >= 1:
        c += ladder_recurs(n-1)
    
    return c

print(ladder_recurs(2))
print(ladder_recurs(3))
print(ladder_recurs(4))
print(ladder_recurs(5))
print(ladder_recurs(8))