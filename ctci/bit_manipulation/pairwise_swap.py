"""
Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

101101 = 1 + 0 + 4 + 8 + 0 + 32 = 45
-> 101110
-> 101110
-> 011110 = 0 + 2 + 4 + 8 + 16 + 0 = 30
"""


def rshift(val, n):
    if val >= 0:
        return val >> n
    elif n == 0:
        return val
    return (val + 0x10000000) >> n


def pairwise_swap(number):
    return ((number & 0xaaaaaaaa) >> 1) | ((number & 0x55555555) << 1)
