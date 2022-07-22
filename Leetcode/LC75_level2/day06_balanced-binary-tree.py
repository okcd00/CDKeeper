"""
https://leetcode.cn/problems/balanced-binary-tree/

给定一个二叉树，判断它是否是高度平衡的二叉树。=
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lef_depth = self.depth(root.left)
        rig_depth = self.depth(root.right)
        # print(root.val, lef_depth, rig_depth)
        if lef_depth == -1:
            return -1
        if rig_depth == -1:
            return -1
        if abs(lef_depth - rig_depth) <= 1:
            return max(lef_depth, rig_depth) + 1
        return -1
