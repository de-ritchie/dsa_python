"""
Minimum Count

Given an integer N, find and return the count of minimum numbers required to represent N as a sum of squares.
That is, if N is 4, then we can represent it as : {1^2 + 1^2 + 1^2 + 1^2} and {2^2}. 
The output will be 1, as 1 is the minimum count of numbers required to represent N as sum of squares.

Input 1 :
12
Output 1 :
3
Explanation of Output 1 :
12 can be represented as : 
A) (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2)

B) (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2) + (1^2)  + (2 ^ 2)

C) (1^2) + (1^2) + (1^2) + (1^2) + (2 ^ 2) + (2 ^ 2)

D) (2 ^ 2) + (2 ^ 2) + (2 ^ 2)

As we can see, the output should be 3.


Input 2 :
9
Output 2 :
1
"""

def min_count_dp(n, mappie):
	if n == 0:
		return 0

	i = 1
	res = None

	if not mappie.get(n, None) is None:
		return mappie[n]

	while i*i <= n:
		tmp  = min_count_dp(n - i*i, mappie)
		if res is None:
			res = tmp
		else:
			res = min(res, tmp)

		i += 1
	
	res += 1
	
	mappie[n] = res

	return res

def min_count(n) :
	#Your code goes here

	#mappie = {}
	#return min_count_dp(n, mappie)

	if n == 0:
		return 0
	
	arr = [0]

	for i in range(1, n + 1):
		j = 1
		minima = None
		while j * j <= i:
			tmp = arr[i - j*j]
			if minima is None:
				minima = tmp
			else:
				minima = min(minima, tmp)
				j += 1
		
		arr.append(1 + minima)
	
	return arr[n]