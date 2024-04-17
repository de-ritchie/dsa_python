"""
Double Modular

You are given a 0-indexed 2D array variables where variables[i] = [ai, bi, ci, mi], and an integer target.
An index i is good if the following formula holds:
0 <= i < variables.length
((ai^bi % 10)^ci) % mi == target
Return an array consisting of good indices in any order.

Example 1:
Input: variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
Output: [0,2]
Explanation: For each index i in the variables array:
1) For the index 0, variables[0] = [2,3,3,10], (23 % 10)3 % 10 = 2.
2) For the index 1, variables[1] = [3,3,3,1], (33 % 10)3 % 1 = 0.
3) For the index 2, variables[2] = [6,1,1,4], (61 % 10)1 % 4 = 2.
Therefore we return [0,2] as the answer.

Example 2:
Input: variables = [[39,3,1000,1000]], target = 17
Output: []
Explanation: For each index i in the variables array:
1) For the index 0, variables[0] = [39,3,1000,1000], (393 % 10)1000 % 1000 = 1.
Therefore we return [] as the answer.

Ref: https://leetcode.com/problems/double-modular-exponentiation/description/
"""

def cust_pow(a, b, m):
    
    res = 1

    while b > 0:
        
        a %= m
        if b & 1 == 1:
            res *= a
            res %= m
        
        b = b >> 1
        a *= a
    
    return res

def double_expo(a, b, c, m):

    r1 = cust_pow(a, b, 10)
    r2 = cust_pow(r1, c, m)

    return r2

def get_good_indices(variables, target):

    res = []

    for i, variable in enumerate(variables):
        a, b, c, m = variable
        if double_expo(a, b, c, m) == target:
            res.append(i)
    
    return res

print(cust_pow(2, 3, 5))
print(cust_pow(2, 5, 13))

print(get_good_indices([[2,3,3,10],[3,3,3,1],[6,1,1,4]], 2))
print(get_good_indices([[39,3,1000,1000]], 17))