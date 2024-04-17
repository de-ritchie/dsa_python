"""
Left Shift => num, shift = num * 2^(shift)
Right Shift => num, shift = num / (2^(shift))

Get ith bit
Set ith bit
Clear ith bit
Update ith bit
Clear last i bits
"""

def left_shift(num, shift):
    return num << shift

def right_shift(num, shift):
    return num >> shift

def bitwise_not(num):
    return ~num

def get_ith_bit(num, i):
    return 1 if left_shift(1, i) & num > 0 else 0

def set_ith_bit(num, i):
    return left_shift(1, i) | num

def clear_ith_bit(num, i):
    return ~(left_shift(1, i)) & num

def clear_ith_bit_alt(num, i):
    mask = left_shift(1, i)
    res = num ^ mask
    return res if res & mask == 0 else num

def update_ith_bit(num, i, v):
    res = clear_ith_bit(num, i)
    return res if v == 0 else res | left_shift(1, i)

def clear_last_i_bits(num, i):
    return left_shift(bitwise_not(0), i) & num


print('Left Shift', left_shift(5, 2))
print('Left Shift', left_shift(1, 3))
print('Right Shift', right_shift(10, 2))
print('Bitwise Not', bitwise_not(10))
print('Bitwise Not & same number', bitwise_not(10) & 10)
print('Bitwise Not | same number', bitwise_not(10) | 10)
print('Bitwise Not & Left shift', left_shift(bitwise_not(10), 1))
print('Bitwise Not & Right shift', right_shift(bitwise_not(10), 1))

print('Get ith bit', get_ith_bit(10, 3))
print('Get ith bit', get_ith_bit(10, 2))
print('Get ith bit', get_ith_bit(10, 1))
print('Get ith bit', get_ith_bit(10, 0))

print('Set ith bit', set_ith_bit(10, 0))
print('Set ith bit', set_ith_bit(10, 2))

print('Clear ith bit', clear_ith_bit(21, 2))
print('Clear ith bit', clear_ith_bit(21, 1))

print('Clear ith bit Alt', clear_ith_bit_alt(21, 2))
print('Clear ith bit Alt', clear_ith_bit_alt(21, 1))

print('Update ith bit', update_ith_bit(21, 2, 0))
print('Update ith bit', update_ith_bit(21, 1, 1))
print('Update ith bit', update_ith_bit(21, 1, 0))

print('Clear last i bits', clear_last_i_bits(21, 3))
print('Clear last i bits', clear_last_i_bits(21, 2))
print('Clear last i bits', clear_last_i_bits(21, 0))