"""
https://leetcode.cn/problems/path-sum-iii/

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
"""


from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(r, val):
            # val: the value_sum when root reaches this node
            ret = prefix.get(val - targetSum, 0)

            # for the nodes in this subtree, prefix_sum has this val
            prefix[val] += 1

            # dfs on child nodes
            if r.left:
                ret += dfs(r.left, r.left.val + val)
            if r.right:
                ret += dfs(r.right, r.right.val + val)
            
            # this routine is over, rollback the prefix_sum dict
            prefix[val] -= 1
            return ret
        
        ans = dfs(root, root.val)
        return ans