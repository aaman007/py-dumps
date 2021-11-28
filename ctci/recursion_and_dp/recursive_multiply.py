"""
Recursive Multiply: Write a recursive function to multiply two positive integers without using
the * operator (or / operator) . You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations.


5  = 00101
6  = 00110
---------
30 = 11110


  101
x 110

101 x 0 =   000
101 x 1 =  1010
101 x 1 = 10100
-----------------
        = 11110
"""


# Naive
def recursive_multiply(a: int, b: int):
    total = 0
    while b:
        total += a
        b -= 1
    return total


# Bit Manipulation
def recursive_multiply_bit(a: int, b: int):
    if not b:
        return 0
    return a * (b % 2) + recursive_multiply_bit(a << 1, b // 2)


# Divide and Conquer
def recursive_multiply_book(a: int, b: int):
    return recursive_multiply_book_helper(min(a, b), max(a, b))


def recursive_multiply_book_helper(smaller: int, bigger: int):
    if not smaller:
        return bigger
    elif smaller == 1:
        return bigger
    half = recursive_multiply_book_helper(smaller >> 1, bigger)
    return half + half + bigger if (smaller & 1) else half + half
