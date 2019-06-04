"""LC300. Longest Increasing Subsequence
Medium

URL: https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, 
find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], 
therefore the length is 4. 

Note:
There may be more than one LIS combination, 
it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class SolutionRecur(object):
    def _LISBigger(self, prev, nums):
        if not nums:
            return 0
        
        lis = self._LISBigger(prev, nums[1:])
        if nums[0] > prev:
            lis_with = 1 + self._LISBigger(nums[0], nums[1:])
            if lis_with > lis:
                lis = lis_with
        return lis

    def lengthOfLIS(self, nums):
        """Length of LIS by recursion.

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        return self._LISBigger(-float('inf'), nums)


class SolutionDp(object):
    def lengthOfLIS(self, nums):
        """Length of LIS by dynamic programming.
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n^2), where n is the length of the nums.
        Space complexity: O(n).
        """
        if not nums:
            return 0

        # Create a table and set all elements to 1,
        # because the LIS of each element is at least 1.
        T = [1] * len(nums)

        # Apply two pointer method: if element j is smaller than element i,
        # update T[i] = max(T[i], T[j] + 1).
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    T[i] = max(T[i], T[j] + 1)

        # Return max elements of table as LIS. 
        return max(T)


def main():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print SolutionRecur().lengthOfLIS(nums)
    print SolutionDp().lengthOfLIS(nums)


if __name__ == '__main__':
    main()
