"""
Sudoku Solver

Ref: https://leetcode.com/problems/sudoku-solver/description/
"""

def is_safe(x, y, num, n, board):

    # Check horizontlly & vertically
    for i in range(n):
        if board[i][y] == num and i != x:
            return False
        if board[x][i] == num and i != y:
            return False
    
    # Check the grid
    start = 0 if x <= 2 else 3 if x <= 5 else 6
    end = 0 if y <= 2 else 3 if y <= 5 else 6

    for i in range(start, start+3):
        for j in range(end, end + 3):
            if board[i][j] == num and i != x and j != y:
                return False
    
    return True

def recurs(i, j, n, board):

    # Base case
    if i == n:
        return True
    
    # Recursive case
    if j == n:
        return recurs(i+1, 0, n, board)

    if board[i][j] == '.':
        for k in range(1, 10):
            if is_safe(i, j, str(k), n, board):
                board[i][j] = str(k)
                if recurs(i, j + 1, n, board):
                    return True
                board[i][j] = '.'
    else:
        return recurs(i, j+1, n, board)
    
    return False

def solve_sudoku(board):
    n = len(board)
    recurs(0, 0, n, board)

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solve_sudoku(board)
print(board)