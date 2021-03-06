"""Leetcode 11. Container With Most Water
Medium

URL: https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a 
point at coordinate (i, ai). n vertical lines are drawn such that the two 
endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container 
contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49 (= 7 * (8 - 1))
"""

class SolutionTwoPointers(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Two pointers from the widest container.
        max_area = 0
        i, j = 0, len(height) - 1

        while i < j:
            h_left, h_right = height[i], height[j]

            # Compute the area based on shorter height.
            h_min = min(h_left, h_right)
            max_area = max(max_area, (j - i) * h_min)

            # Move shorter height toward middle to find bigger area.
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


def main():
    # Output: 49 = (8 - 1) * 7
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print SolutionTwoPointers().maxArea(height)


if __name__ == '__main__':
    main()
