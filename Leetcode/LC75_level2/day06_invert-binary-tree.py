"""
https://leetcode.cn/problems/invert-binary-tree/submissions/

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root 