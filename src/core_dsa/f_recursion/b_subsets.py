"""
Subsets of String

Example 1:
Input : abc
Output : "", a, b, c, ab, bc, ac, abc
"""

def subsequence(s, curr, i):

    if len(s) == i:
        print(curr)
        return
    
    subsequence(s, curr + s[i], i + 1)
    subsequence(s, curr, i + 1)

subsequence('abc', '', 0)
subsequence('abcd', '', 0)