"""
Longest Substring without repeating characters

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def len_of_longest_substr(txt):

    mapper = {}
    i = 0
    max_len = 0

    for j, c in enumerate(txt):
        
        if c in mapper:
            if i <= mapper[c]:
                i = mapper[c] + 1

        mapper[c] = j
        max_len = max(max_len, j - i + 1)
        # print('max_len', max_len, i, j, c)
    
    return max_len


print(len_of_longest_substr('abcabcbb'))
print(len_of_longest_substr('bbbbb'))
print(len_of_longest_substr('pwwkew'))
print(len_of_longest_substr('abba'))
print(len_of_longest_substr('tmmzuxt'))