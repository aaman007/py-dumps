"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
Hints: # 106, #121, #134, #136
"""

from collections import Counter


def is_palindrome_permutation(text):
    freq = Counter(text.lower())
    odd = 0

    for key in freq:
        if key == ' ':
            continue
        elif freq[key] & 1:
            odd += 1

    return odd <= 1


def is_palindrome_permutation_bitwise(text):
    xor = 0

    for ch in text.lower():
        if ch == ' ':
            continue
        order = ord(ch) - ord('a')
        xor ^= 1 << order

    return bin(xor).count('1') <= 1
