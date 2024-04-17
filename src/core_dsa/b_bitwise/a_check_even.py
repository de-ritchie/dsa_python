"""
Check if a number is Even or Odd
"""

def check_even_or_odd(x):
    return 'Odd' if x & 1 == 1 else 'Even'

print(check_even_or_odd(5))
print(check_even_or_odd(15))
print(check_even_or_odd(51))
print(check_even_or_odd(56))