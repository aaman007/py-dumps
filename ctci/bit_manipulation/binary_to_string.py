"""
Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately in binary with at
most 32 characters, print "ERROR:'

-> binary_to_string(0.625) = '.101'
"""


def binary_to_string(number):  # number = 0.0 - 1.0
    if number >= 1 or number <= 0:
        return "ERROR"

    result = ['.']
    while number > 0:
        if len(result) >= 32:
            return "ERROR"

        r = number * 2
        if r >= 1:
            result.append('1')
            number = r - 1
        else:
            result.append('0')
            number = r

    return ''.join(result)
