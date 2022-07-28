"""
https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

给定一个二叉搜索树的根节点 root ，和一个整数 k ，
请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        stack = [root]
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.append(i.right)
                stack.append(i.val)
                stack.append(i.left)
            if isinstance(i, int):
                if count == k:
                    return i
                count += 1

    def kthSmallest_v2(self, root: Optional[TreeNode], k: int) -> int:

        def inOrderTraverse(node):
            if node:
                yield from inOrderTraverse(node.left)
                yield node.val
                yield from inOrderTraverse(node.right)
                
        ans = inOrderTraverse(root)
        for i in range(k-1):
            next(ans)
        return next(ans)
