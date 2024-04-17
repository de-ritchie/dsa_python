"""
Longest Common Subsequence

Given two strings, 'S' and 'T' with lengths 'M' and 'N', find the length of the 'Longest Common Subsequence'.
For a string 'str'(per se) of length K, 
the subsequences are the strings containing characters in the same relative order as they are present in 'str,' but not necessarily contiguous. 
Subsequences contain all the strings of length varying from 0 to K.

Example :
Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc.

Sample Input 1 :
adebc
dcadb
Sample Output 1 :
3
Explanation of the Sample Output 1 :
Both the strings contain a common subsequence 'adb', which is the longest common subsequence with length 3. 

Sample Input 2 :
ab
defg
Sample Output 2 :
0
Explanation of the Sample Output 2 :
The only subsequence that is common to both the given strings is an empty string("") of length 0.

"""

def lcs_recurs(s, t):

    if len(s) == 0 or len(t) == 0:
        return 0
    
    if s[0] == t[0]:
        return 1 + lcs_recurs(s[1:], t[1:])
    
    return max(
        lcs_recurs(s, t[1:]),
        lcs_recurs(s[1:], t)
    )

def lcs_dp_memo(s, t, i, j, matrix):

    if i >= len(s) or j >= len(t):
        return 0
    
    if matrix[i][j] == -1:
        if s[i] == t[j]:
            matrix[i][j] = 1 + lcs_dp_memo(s, t, i + 1, j + 1, matrix)
        else:
            matrix[i][j] = max(
                lcs_dp_memo(s, t, i, j + 1, matrix),
                lcs_dp_memo(s, t, i + 1, j, matrix)
            )

    return matrix[i][j]

def lcs_dp_iter(s, t):

    m = len(s)
    n = len(t)
    matrix = [[-1 if i < m and j < n else 0 for j in range(n + 1)] for i in range(m + 1)]
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):

            if s[i] == t[j]:
                matrix[i][j] = 1 + matrix[i + 1][j + 1]
            else:
                matrix[i][j] = max(
                    matrix[i + 1][j],
                    matrix[i][j + 1]
                )
    
    return matrix[0][0]