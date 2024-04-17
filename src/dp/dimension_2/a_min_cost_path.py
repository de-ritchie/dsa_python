"""
Minimum Cost Path

An integer matrix of size (M x N) has been given. 
Find out the minimum cost to reach from the cell (0, 0) to (M - 1, N - 1).
From a cell (i, j), you can move in three directions:
1. ((i + 1),  j) which is, "down"
2. (i, (j + 1)) which is, "to the right"
3. ((i+1), (j+1)) which is, "to the diagonal"

Sample Input 1 :
3 4
3 4 1 2
2 1 8 9
4 7 8 1
Sample Output 1 :
13

Sample Input 2 :
3 4
10 6 9 0
-23 8 9 90
-200 0 89 200
Sample Output 2 :
76

Sample Input 3 :
5 6
9 6 0 12 90 1
2 7 8 5 78 6
1 6 0 5 10 -4 
9 6 2 -10 7 4
10 -2 0 5 5 7
Sample Output 3 :
18
"""

def min_cost_path_recurs(matrix, row, col, i, j):

    if i >= row and j >= col:
        return 0
    
    min_path = float('inf')

    if i + 1 < row:
        min_path = min(min_path, min_cost_path_recurs(matrix, row, col, i + 1, j))
    if j + 1 < col:
        min_path = min(min_path, min_cost_path_recurs(matrix, row, col, i, j + 1))
    if i + 1 < row and j + 1 < col: 
        min_path = min(min_path, min_cost_path_recurs(matrix, row, col, i + 1, j + 1))
    
    if i + 1 >= row and j + 1 >= col:
        return matrix[i][j]

    return matrix[i][j] + min_path

def min_cost_path_dp_memo(matrix, row, col, i, j, dp_matrix):

    if dp_matrix[i][j] != -1:
        return dp_matrix[i][j]

    min_path = float('inf')

    if i + 1 < row:
        min_path = min(min_path, min_cost_path_dp_memo(matrix, row, col, i + 1, j, dp_matrix))
    if j + 1 < col:
        min_path = min(min_path, min_cost_path_dp_memo(matrix, row, col, i, j + 1, dp_matrix))
    if i + 1 < row and j + 1 < col: 
        min_path = min(min_path, min_cost_path_dp_memo(matrix, row, col, i + 1, j + 1, dp_matrix))
    
    if i + 1 >= row and j + 1 >= col:
        dp_matrix[i][j] = matrix[i][j]
        return dp_matrix[i][j]

    dp_matrix[i][j] = matrix[i][j] + min_path
    return dp_matrix[i][j]

def min_cost_path_dp_iter(matrix, row, col):

    dp_matrix = [[-1 for j in range(col)] for i in range(row)]

    dp_matrix[row - 1][col - 1] = matrix[row - 1][col - 1]

    for i in range(row - 1, -1, -1):
        for j in range(col - 1, -1, -1):

            if i == row - 1 and j == col - 1:
                continue

            min_path = None

            if i + 1 < row:
                min_path = dp_matrix[i + 1][j]
            if j + 1 < col:
                path = dp_matrix[i][j + 1]
                min_path =  path if min_path is None else min(min_path, path)
            if i + 1 < row and j + 1 < col: 
                path = dp_matrix[i + 1][j + 1]
                min_path =  path if min_path is None else min(min_path, path)
            
            dp_matrix[i][j] = matrix[i][j] + min_path
    
    return dp_matrix[0][0]