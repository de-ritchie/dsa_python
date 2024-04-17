"""
Count set bits

Example:
Input: 10
Output: 2
Explanation: 1010 => 2
"""

def count_set_bits(num):
    c = 0
    while num > 0:
        if num & 1:
            c += 1
        num = num >> 1
    
    return c

def count_set_bits_alt(num):
    c = 0
    while num > 0:
        num = num & (num - 1)
        c += 1
    return c

print(count_set_bits(10))
print(count_set_bits(21))
print(count_set_bits(58))

print(count_set_bits_alt(10))
print(count_set_bits_alt(21))
print(count_set_bits_alt(58))