"""
Keypad Combination

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Ref: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1149788880/
"""

digit_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def letter_comb(digits, i, curr, res):

    if len(digits) == i:
        if i > 0:
            res.append(curr)
        return res

    for letter in digit_map[digits[i]]:
        letter_comb(digits, i + 1, curr + letter, res)
    
    return res
    

print(letter_comb("", 0, "", []))
print(letter_comb("23", 0, "", []))
print(letter_comb("2", 0, "", []))
