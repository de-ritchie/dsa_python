"""
Min Steps to One

Given a positive integer 'n', find and return the minimum number of steps that 'n' has to take to get reduced to 1. 
You can perform any one of the following 3 steps:
1.) Subtract 1 from it. (n = n - 1) ,
2.) If its divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
3.) If its divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ).  


Input 1 :
4
Output 1 :
2 
Explanation of Output 1 :
For n = 4
Step 1 :  n = 4 / 2  = 2
Step 2 : n = 2 / 2  =  1

Input 2 :
7
Output 2 :
3
Explanation of Output 2 :
For n = 7
Step 1 :  n = 7 - 1 = 6
Step 2 : n = 6  / 3 = 2 
Step 3 : n = 2 / 2 = 1
"""

def count_min_steps_to_one_dp(n, arr) :
	
	if n == 1:
		return 0
	
	if arr[n] != -1:
		return arr[n]

	minima = 1 + count_min_steps_to_one_dp(n - 1, arr)

	if n % 2 == 0:
		tmp = 1 + count_min_steps_to_one_dp(n//2, arr)
		minima = min(minima, tmp)
	
	if n % 3 == 0:
		tmp = 1 + count_min_steps_to_one_dp(n//3, arr)
		minima = min(minima, tmp)
	
	arr[n] = minima

	return minima

def count_min_steps_to_one(n) :
	#Your code goes here

	# arr = [-1 for i in range(n + 1)]
	# return count_min_steps_to_one_dp(n, arr)

	arr = [0]
	arr.append(0)

	for i in range(2, n + 1):
		
		minima = 1 + arr[i - 1]
		if i % 2 == 0 :
			minima = min(minima, 1 + arr[i//2])
		if i % 3 == 0 :
			minima = min(minima, 1 + arr[i//3])
		
		arr.append(minima)

	return arr[n]