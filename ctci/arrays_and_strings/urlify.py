"""
URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith
Output: "Mr%20John%20Smith"

Python Example - BECAUSE STRINGS ARE IMMUTABLE:
    ['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' '], 13
    ['M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h']
"""


class Solution:
    def urlify(self, text_list, true_length):
        idx = len(text_list) - 1
        for i in range(true_length - 1, -1, -1):
            if text_list[i] == ' ':
                text_list[idx-2:idx+1] = ['%', '2', '0']
                idx -= 3
            else:
                text_list[idx] = text_list[i]
                idx -= 1
        return text_list
