"""
Permutations without Dups: Write a method to compute all permutations of a string of unique
characters.
"""


def permutations_of_unique_string(s: str):
    return find_permutations(s, set())


def find_permutations(s, taken):
    if len(taken) == len(s):
        return ['']

    result = []
    for index, ch in enumerate(s):
        if index in taken:
            continue
        taken.add(index)
        result.extend([ch + permutation for permutation in find_permutations(s, taken)])
        taken.remove(index)

    return result
