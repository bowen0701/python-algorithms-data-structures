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
    def _LIS_bigger(self, prev, nums, start, end):
        if start == end:
            return 0

        # The LIS of nums[0:n] is either a LIS of nums[1:n], without nums[0]. 
        lis = self._LIS_bigger(prev, nums, start + 1, end)

        # Or the LIS is 1 + a LIS of nums[1:n], with nums[0], 
        # if nums[0] is bigger than the previous. Update the LIS if suitable.
        if nums[start] > prev:
            lis_with = 1 + self._LIS_bigger(nums[start], nums, start + 1, end)
            if lis_with > lis:
                lis = lis_with
        return lis

    def lengthOfLIS(self, nums):
        """Length of LIS by recursion.

        Time complexity: O(2^n).
        Space complexity: O(1).
        """
        start, end = 0, len(nums) - 1
        return self._LIS_bigger(-float('inf'), nums, start, end)


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


class SolutionBinarySearch(object):
    def lengthOfLIS(self, nums):
        """Length of LIS by binary search.
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n*logn), where n is the length of the nums.
        Space complexity: O(n).
        """
        if not nums:
            return 0

        tails = [0] * len(nums)
        lis = 0

        for n in nums:
            left, right = 0, lis
            while left != right:
                mid = (left + right) // 2
                if tails[mid] < n:
                    left = mid + 1
                else:
                    right = mid

            tails[left] = n
            lis = max(left + 1, lis)
        return lis


def main():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print SolutionRecur().lengthOfLIS(nums)
    print SolutionDp().lengthOfLIS(nums)
    print SolutionBinarySearch().lengthOfLIS(nums)


if __name__ == '__main__':
    main()
