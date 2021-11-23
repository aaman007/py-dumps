"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
"""


def is_substring(s1: str, s2: str) -> bool:
    """ Naive cause its provided, otherwise hashing or kmp will be required """
    return s1 in s2 or s2 in s1


def is_rotation(s1: str, s2: str) -> bool:
    return s1 and len(s1) == len(s2) and is_substring(s1 * 2, s2)
