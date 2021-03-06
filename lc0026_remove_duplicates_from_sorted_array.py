"""Leetcode 26. Remove Duplicates from Sorted Array
Easy

URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums
being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification
to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

class SolutionTailIter(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n), where n is the lenght of nums.
        Space complexity: O(1).
        """
        # Use pos to store the distinct elements.
        pos = 0
        for i in range(1, len(nums)):
            # When see a distinct num, increment pos and replace it by num.
            if nums[i] != nums[pos]:
                pos += 1
                nums[pos] = nums[i]

        new_len = pos + 1
        return new_len


def main():
    # Output: 2.
    nums = [1, 1, 2]
    print SolutionTailIter().removeDuplicates(nums)

    # Output: 5.
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print SolutionTailIter().removeDuplicates(nums)


if __name__ == '__main__':
    main()
