"""
https://leetcode.cn/problems/diameter-of-binary-tree/

给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
这条路径可能穿过也可能不穿过根结点。
注意：两结点之间的路径长度是以它们之间边的数目表示。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter

    def depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lef_depth = self.depth(root.left)
        rig_depth = self.depth(root.right)
        # print(root.val, lef_depth, rig_depth)
        diameter = lef_depth + rig_depth
        if diameter > self.diameter:
            self.diameter = diameter
        return max(lef_depth, rig_depth) + 1
