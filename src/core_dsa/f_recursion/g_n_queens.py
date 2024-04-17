"""
N Queens
"""

def is_safe(x, y, n, board):
    
    # Check Vertically
    i = x - 1
    while i >=0:
        if board[i][y] == 'Q':
            return False
        i -= 1
    
    # Check Diagonally Left
    i = x - 1
    j = y - 1
    while i >=0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    # Check Diagonally Right
    i = x - 1
    j = y + 1
    while i >=0 and j >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True

def recurs(i, n, board, res):
    
    # Base case
    if i == n:
        # for x in board:
        #     print(x)
        # print('-'*5)
        res.append([''.join(box) for box in board])
        return
    
    for j in range(n):
        if is_safe(i, j, n, board):
            board[i][j] = 'Q'
            recurs(i+1, n, board, res)
            board[i][j] = '.'
    
    return

def n_queens(n):

    board = [['.' for j in range(n)] for i in range(n)]
    res = []

    for i in range(n):
        if i == 0 or (i - 1 > 0 and 'Q' in board[i - 1]):
            recurs(i, n, board, res)
    
    return res

print(n_queens(1))
print(n_queens(2))
print(n_queens(4))
print(n_queens(5))