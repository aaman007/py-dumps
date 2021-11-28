"""
Permutations with Duplicates: Write a method to compute all permutations of a string whose
characters are not necessarily unique. The list of permutations should not have duplicates.
"""


def permute(s: str):
    return find_permutations(''.join(sorted(s)), set())


def find_permutations(s, taken):
    if len(taken) == len(s):
        return ['']

    result = []
    prev = None
    for index, ch in enumerate(s):
        if prev == ch or index in taken:
            continue

        prev = ch
        taken.add(index)
        result.extend([ch + permutation for permutation in find_permutations(s, taken)])
        taken.remove(index)

    return result

