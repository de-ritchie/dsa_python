"""
Permutation

Ref: https://www.hackerearth.com/problem/algorithm/strings-permutations/
"""

def permute(s, curr):

    # print('-----', s, curr, len(s))
    if len(s) == 1:
        print(curr + s)
        return

    for i, c in enumerate(s):
        permute(s[0:i]+s[i+1:], curr + c)


permute("ab", "")
permute("abc", "")
permute("abcd", "")
permute("abcde", "")