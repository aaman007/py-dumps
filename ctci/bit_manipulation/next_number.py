"""
Next Number: Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation .
"""


def get_prev(number):
    c = number
    c0, c1 = 0, 0

    while c & 1:
        c1 += 1
        c >>= 1

    if not c:
        return -1

    while c and not (c & 1):
        c0 += 1
        c >>= 1

    p = c0 + c1  # position of rightmost non-trailing zero

    number &= ((~0) << (p + 1))  # clears from bit p onwards
    mask = (1 << (c1 + 1)) - 1  # Sequence of (cl+l) ones
    number |= mask << (c0 - 1)

    return number


def get_next(number):
    c = number
    c0, c1 = 0, 0

    while c and not (c & 1):
        c0 += 1
        c >>= 1
    while c & 1:
        c1 += 1
        c >>= 1

    if c1 + c0 == 31 or not (c1 + c0):
        return -1

    p = c0 + c1  # position of rightmost non-trailing zero

    number |= (1 << p)  # Flip rightmost non-trailing zero
    number &= ~((1 << p) - 1)  # Clear all bits to the right of p
    number |= (1 << (c1 - 1)) - 1  # Insert (e1-1) ones on the right.

    return number


def next_number(number):
    return get_prev(number), get_next(number)
