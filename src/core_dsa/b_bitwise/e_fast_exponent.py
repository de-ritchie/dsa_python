"""
Fast Exponentiation

Input: 3^5
Output: 243
"""

def fast_expo(num, pow):
    
    res = 1
    c = 1

    while pow > 0:
        if pow & 1 == 1:
            res *= num**c
        c *= 2
        pow = pow >> 1
    
    return res

print(fast_expo(5, 5))
print(fast_expo(3, 5))