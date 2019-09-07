"""Leetcode 198. House Robber
Easy

URL: https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will
automatically contact the police if two adjacent houses were broken into
on the same night.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight
without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and
             rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

class SolutionRecur(object):
    def _recur(self, nums, n):
        if n < 0:
            return 0

        # To rob or not to rob house n:
        # T[n] = max(nums[n] + T[n-2], T[n-1]).
        amount_in_n = nums[n] + self._recur(nums, n - 2)
        amount_ex_n = self._recur(nums, n - 1)
        return max(amount_in_n, amount_ex_n)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        # Apply top-down recursion.
        if not nums:
            return 0

        return self._recur(nums, len(nums) - 1)


def main():
    # Output: 4.
    nums = [1,2,3,1]
    print SolutionRecur().rob(nums)

    # Outpyt: 12.
    nums = [2,7,9,3,1]
    print SolutionRecur().rob(nums) 


if __name__ == '__main__':
    main()
