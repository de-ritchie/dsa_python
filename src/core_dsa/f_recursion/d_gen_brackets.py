"""
Generate Brackets

Example 1:
Input: 3
Output: ((())), ()(()), (())(), (()()), ()()()

Ref: https://leetcode.com/problems/generate-parentheses/description/
"""

def gen_brackets(n, curr, ob, cb):

    if 2 * n == len(curr):
        print(curr)
        return
    
    if ob < n:
        gen_brackets(n, curr+"(", ob + 1, cb)
    if ob > cb:
        gen_brackets(n, curr+")", ob, cb+1)

gen_brackets(1, "", 0, 0)
gen_brackets(2, "", 0, 0)
gen_brackets(3, "", 0, 0)