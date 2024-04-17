"""
Maze Problem

You are provided a matrix of size N*N with source position at (0,0) and destination at (N-1,N-1) in a 2D array. 
Some of the positions in the array are marked as 0 which are blocked cells, rest being marked 1.

A path is a connected sequence of elements from (0,0) to (N-1,N-1) which consists of 1. 
A sequence of 1s in the 2D array is connected if every 1 in the sequence is adjacent (the above or left neighbour) to the next 1 in the sequence.

For example, in the following matrix,

'1' '1'  0
 0  '1' '1'
 1   0  '1'

the 1s marked in quotes is a connected path from (0,0) to (2,2)

Note that cells at (0,0) and (N-1,N-1) are always 1. 
You can either make movement towards right or down, i.e., 
from position (x,y), you can go to either the position (x,y+1) or (x+1,y).

Input
First line consists of the number of test cases and second line consist of size of the input array N (<=50), 
following that would be the state of NxN maze which would consist of 0s and 1s.

Output
You have to print "POSSIBLE" if there exists a path between the source and the destination otherwise print "NOT POSSIBLE".

Ref: https://www.hackerearth.com/problem/algorithm/problem-1-29/
"""

def recurs(i, j, n, grid):

    # Base case
    if i == n:
        return True
    
    # Recursive cases

    if j == n:
        return recurs(i + 1, 0, n, grid)
    
    if grid[i][j] == 1:
        r1 = recurs(i, j + 1, n, grid)
        r2 = recurs(i + 1, j, n, grid)

        return r1 or r2
    return False

def solve_maze(grid):
    return recurs(0, 0, len(grid), grid)

print(solve_maze([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
print(solve_maze([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))