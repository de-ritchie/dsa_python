"""
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

def check_2_dicts(tgt, ref):
    for k, v in tgt.items():
        if k not in ref or v > ref[k]:
            return False
    return True

def min_window(s, t):

    mapper = {}
    tracker = {}
    i = 0
    min_win = ""

    for c in t:
        mapper[c] = mapper.get(c, 0) + 1

    for j, c in enumerate(s):

        tracker[c] = tracker.get(c, 0) + 1
        # print('-----', i, j, tracker)
        
        while i<=j and j - i + 1 >= len(t) and check_2_dicts(mapper, tracker):
            
            if min_win == "":
                min_win = s[i: j + 1]
            else:
                if len(min_win) > j - i + 1:
                    min_win = s[i: j + 1]
            
            if tracker[s[i]] > 1:
                tracker[s[i]] -= 1
            else:
                del tracker[s[i]]
            
            i += 1

    # print(tracker, mapper)
    return min_win


print(min_window("ADOBECODEBANC", "ABC"))
print(min_window("a", "a"))
print(min_window("a", "aa"))