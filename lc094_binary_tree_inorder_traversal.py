"""Leetcode 94. Binary Tree Inorder Traversal
Medium

URL: https://leetcode.com/problems/binary-tree-inorder-traversal/

Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def inorder_util(self, root, nodes):
        if root:
            self.inorder_util(root.left, nodes)
            nodes.append(root.val)
            self.inorder_util(root.right, nodes)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        self.inorder_util(root, nodes)
        return nodes


def main():
    # Input: [1,null,2,3]
    # 1
    #  \
    #   2
    #  /
    # 3
    # Output: [1,3,2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print SolutionRecur().inorderTraversal(root)  


if __name__ == '__main__':
    main()
