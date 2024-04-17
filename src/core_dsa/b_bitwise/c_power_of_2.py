"""
Find if a number is power of 2
"""

def is_power_of_2(num):
    return num & (num - 1) == 0

print(is_power_of_2(16))
print(is_power_of_2(13))
print(is_power_of_2(32))
print(is_power_of_2(256))
print(is_power_of_2(144))