"""Leetcode 572. Subtree of Another Tree
Easy

URL: https://leetcode.com/problems/subtree-of-another-tree/

Given two non-empty binary trees s and t,
check whether tree t has exactly the same structure and node values
with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionPreorder(object):
    def _isMatch(self, s, t):
        if not s or not t:
            return s is t
            
        return (s.val == t.val and 
                self._isMatch(s.left, t.left) and 
                self._isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool

        Time complexity: O(|s|*|t|), where 
          - |s| is the number of nodes in s.
        Space complexity: O(h(s)), where h(s) is the height of s.
        """
        # Apply preorder traversal to check match.
        if not s:
            return False

        return (self._isMatch(s, t) or
                self.isSubtree(s.left, t) or 
                self.isSubtree(s.right, t))


def main():
    # Ans: True
    # Given tree s:
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    # Given tree t:
    #    4 
    #   / \
    #  1   2
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    print SolutionPreorder().isSubtree(s, t)

    # Ans: False
    # Given tree s:
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    #     /
    #    0
    # Given tree t:
    #    4
    #   / \
    #  1   2
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    s.left.right.left = TreeNode(0)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    print SolutionPreorder().isSubtree(s, t)

    # Ans: True
    # t = [1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]
    # s = [1,null,1,null,1,null,1,null,1,null,1,2]
    t = TreeNode(1)
    t.right = TreeNode(1)

if __name__ == '__main__':
    main()
