"""Leetcode 279. Perfect Squares
Medium

Given a positive integer n, find the least number of perfect square 
numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int

        Time complexity: O(n*m), where m is squared root of n.
        Space complexity: O(n*m).
        """
        # Compute the max number.
        m = int(pow(n, 0.5))
        sq_nums = [pow(s, 2) for s in range(1, m + 1)]

        T = [[float('inf')] * (n + 1) for s in range(m)]

        # Base case for integer 0.
        for s in range(m):
            T[s][0] = 1

        for s in range(m):
            for i in range(1, n + 1):
                if i == sq_nums[s]:
                    T[s][i] = 1
                elif i > sq_nums[s]:
                    T[s][i] = min(1 + T[s][i - sq_nums[s]], T[s - 1][i])
                else:
                    T[s][i] = T[s - 1][i]

        return T[-1][-1]

def main():
    import time

    n = 12
    print Solution().numSquares(n)

    n = 13
    print Solution().numSquares(n)


if __name__ == '__main__':
    main()