"""
Loot Houses

A thief wants to loot houses. 
He knows the amount of money in each house. He cannot loot two consecutive houses. 
Find the maximum amount of money he can loot.

Sample Input 1 :
6
5 5 10 100 10 5
Sample Output 1 :
110

Sample Input 2 :
6
10 2 30 20 3 50
Sample Output 2 :
90
Explanation of Sample Output 2 :
Looting first, third, and the last houses([10 + 30 + 50]) will result in the maximum loot, 
and all the other possible combinations would result in less than 90
"""

def max_loot_recurs(houses, i):

    if len(houses) <= i:
        return 0
    
    loot1 = houses[i] + max_loot_recurs(houses, i + 2)
    loot2 = max_loot_recurs(houses, i + 1)

    return max(loot1, loot2)

def max_loot_dp_mem(houses, i, arr):

    if len(houses) <= i:
        return 0
    
    if arr[i] == -1:
        loot1 = houses[i] + max_loot_dp_mem(houses, i + 2, arr)
        loot2 = max_loot_dp_mem(houses, i + 1, arr)

        arr[i] = max(loot1, loot2)
    
    return arr[i]

def max_loot_dp_iter(houses, n):

    if n == 0:
        return 0

    loots = [-1 for i in range(n)]
    loots[0] = houses[0]
    loots[1] = max(houses[0], houses[1])

    for i in range(2, n):
        loot1 = houses[i] + loots[i - 2]
        loot2 = loots[i - 1]
        loots[i] = max(loot1, loot2)
    
    print('arr------>', loots)

    return loots[n - 1]