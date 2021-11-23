"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def compress_string_v1(s: str) -> str:
    compressed = [s[0]]
    last, count = s[0], 0

    for ch in s:
        if ch != last:
            compressed.append(str(count))
            compressed.append(str(ch))
            count = 0
        count += 1
        last = ch
    compressed.append(str(count))
    compressed = ''.join(compressed)

    return compressed if len(compressed) < len(s) else s


def compress_string_v2(s: str) -> str:
    compressed, count = [], 0

    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            compressed.append(s[i])
            compressed.append(str(count))
            count = 0

    compressed = ''.join(compressed)
    return compressed if len(compressed) < len(s) else s


def compress_string_v3(s: str) -> str:
    if count_compression_length(s) >= len(s):
        return s

    compressed, count = [], 0
    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            compressed.append(s[i])
            compressed.append(str(count))
            count = 0

    return ''.join(compressed)


def count_compression_length(s: str) -> int:
    total_length, count = 0, 0
    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            total_length += 1 + len(str(count))
            count = 0
    return total_length
