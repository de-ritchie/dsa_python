"""
Byte Landian

Byteland has a very strange monetary system.
Each Bytelandian gold coin has an integer number written on it. 
A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4. 
But these numbers are all rounded down (the banks have to make a profit).
You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. 
But you can not buy Bytelandian coins.
You have one gold coin. What is the maximum amount of American dollars you can get for it?

Sample Input 1 :
12
Sample Output 1 :
13
Explanation of Sample Output 1 :
You can change 12 into 6, 4 and 3, and then change these into $6 + $4 + $3 = $13.

Sample Input 2 :
2
Sample Output 1 :
2
Explanation of Sample Output 2 :
If you try changing the coin 2 into 3 smaller coins, you will get 1, 0 and 0, and later you can get no more than $1 out of them.
It is better just to change the 2 coin directly into $2.
"""

def bytelandian_recurs(n) :
	# Write your code here
    
    if n == 0:
        return 0
    
    d1 = n//2
    d2 = n//3
    d3 = n//4

    d1 = max(bytelandian_recurs(d1), d1)
    d2 = max(bytelandian_recurs(d2), d2)
    d3 = max(bytelandian_recurs(d3), d3)

    return max(d1 + d2 + d3, n)

def bytelandian_recurs_dp(n, arr) :
	# Write your code here
    
    if arr[n] != - 1:
        return arr[n]

    if n == 0:
        arr[0] = 0
        return arr[0]
    
    d1 = n//2
    d2 = n//3
    d3 = n//4

    d1 = max(bytelandian_recurs_dp(d1, arr), d1)
    d2 = max(bytelandian_recurs_dp(d2, arr), d2)
    d3 = max(bytelandian_recurs_dp(d3, arr), d3)

    arr[n] = max(d1 + d2 + d3, n)
    return arr[n]

def bytelandian(n):
    
    arr = [-1 for i in range(n + 1)]
    return bytelandian_recurs_dp(n, arr)

def bytelandian_dp(n):
    
    arr = [-1 for i in range(n + 1)]
    arr[0] = 0
    
    for i in range(1, n+1):
        
        d1 = arr[i//2]
        d2 = arr[i//3]
        d3 = arr[i//4]

        arr[i] = max(d1 + d2 + d3, i)
    
    return arr[n]
