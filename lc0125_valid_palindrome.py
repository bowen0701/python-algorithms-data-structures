"""Leetcode 125. Valid Palindrome
Easy

URL: https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""

class SolutionReverse(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Take lower, convert to list, and keep alphanumetic chars.
        s_ls = [c for c in list(s.lower()) 
                if 0 <= ord(c) - ord('a') <= 25 or 0 <= ord(c) - ord('0') <= 9]

        # Compare list with its reverse.
        return s_ls == s_ls[::-1]


def main():
    # Ans: True
    s = "A man, a plan, a canal: Panama"
    print SolutionReverse().isPalindrome(s)

    # Ans: False
    s = "0P"
    print SolutionReverse().isPalindrome(s)


if __name__ == '__main__':
    main()
