"""Leetcode 8. String to Integer (atoi)
Medium

URL: https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until 
the first non-whitespace character is found. Then, starting from this character, 
takes an optional initial plus or minus sign followed by as many numerical 
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral 
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid 
integral number, or if no such sequence exists because either str is empty or 
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [-2^31, 2^31 - 1].
If the numerical value is out of the range of representable values,
INT_MAX (2^31 - 1) or INT_MIN (-2^31) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the 
minus sign. Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a 
numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a 
numerical digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed 
integer. Thefore INT_MIN (-2^31) is returned.
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove front & back spaces. 
        ls = list(s.strip())

        # Edge case.
        if len(ls) == 0:
            return 0

        # Check if the first char is negative sign.
        if ls[0] == '-':
            sign = -1
        else:
            sign = 1

        if ls[0] in ['-', '+']:
            del ls[0]

        # Iterate through unsigned atoi if char is digit.
        i = 0
        unsigned_atoi = 0

        while i < len(ls) and ls[i].isdigit():
            unsigned_atoi = unsigned_atoi * 10 + int(ls[i])
            i += 1

        atoi = sign * unsigned_atoi

        # Truncate atoi if it is out of integer range.
        return max(-pow(2,31), (min(atoi, pow(2, 31) - 1)))


def main():
    s = '42'
    print(Solution().myAtoi(s))

    s = '   -42'
    print(Solution().myAtoi(s))

    s = '4193 with words'
    print(Solution().myAtoi(s))

    s = 'words and 987'
    print(Solution().myAtoi(s))

    s = '-91283472332'
    print(Solution().myAtoi(s))

    s = ' '
    print(Solution().myAtoi(s))


if __name__ == '__main__':
    main()
