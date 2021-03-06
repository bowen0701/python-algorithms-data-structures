"""Leetcode 345. Reverse Vowels of a String
Easy

URL: https://leetcode.com/problems/reverse-vowels-of-a-string/

Write a function that takes a string as input and reverse only the vowels of
a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
"""

class SolutionReversedVowelPosDict(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not s:
            return ''

        n = len(s)

        # Use set to collect vowels for quick lookup.
        vowels = set(['A', 'E', 'I', 'O', 'U',
                      'a', 'e', 'i', 'o', 'u'])

        # Collect vowles & positions in a dict: pos->vowel, in reversed order.
        vowel_chars = []
        vowel_pos = []
        for pos, c in enumerate(s):
            if c in vowels:
                vowel_chars.append(c)
                vowel_pos.append(pos)

        rev_vowel_pos = dict()
        for i, c in enumerate(reversed(vowel_chars)):
            rev_vowel_pos[vowel_pos[i]] = c

        # Iterate through string list, replace vowel by dict: pos-vowel.
        s_list = list(s)
        for i in range(n):
            if i in rev_vowel_pos:
                s_list[i] = rev_vowel_pos[i]

        return ''.join(s_list)


class SolutionSwapTwoPointers(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not s:
            return ''

        # Use set to collect vowels for quick lookup.
        vowels = set(['A', 'E', 'I', 'O', 'U',
                      'a', 'e', 'i', 'o', 'u'])

        # Since string is immutable.
        s_list = list(s)

        # Apply two pointers method from two sides to swap vowels.
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s_list[i] not in vowels:
                i += 1
            while i < j and s_list[j] not in vowels:
                j -= 1

            if i != j:
                s_list[i], s_list[j] = s_list[j], s_list[i]

                i += 1
                j -= 1

        return ''.join(s_list)


def main():
    # Output: "holle"
    s = "hello"
    print SolutionReversedVowelPosDict().reverseVowels(s)
    print SolutionSwapTwoPointers().reverseVowels(s)

    # Output: "leotcede"
    s = "leetcode"
    print SolutionReversedVowelPosDict().reverseVowels(s)
    print SolutionSwapTwoPointers().reverseVowels(s)

    # Output: "epplA"
    s = "Apple"
    print SolutionReversedVowelPosDict().reverseVowels(s)
    print SolutionSwapTwoPointers().reverseVowels(s)


if __name__ == '__main__':
    main()
