"""
Staircase

A child runs up a staircase with 'n' steps and can hop either 1 step, 2 steps or 3 steps at a time. 
Implement a method to count and return all possible ways in which the child can run-up to the stairs

Input 1:
4
Output 1:
7

Input 2:
10
Output 2:
274
"""

def staircase(n) :
	arr = []
	
	arr.append(0)
	arr.append(1)
	arr.append(2)
	arr.append(4)

	for i in range(4, n + 1):
		arr.append(
			arr[i-1] + arr[i - 2] + arr[i - 3]
		)

	return arr[n]