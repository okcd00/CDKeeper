# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ret = [root.val]
        cur_cnt, cur_sum = 0, 0.
        q = []
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
        q.append('end')
        while q.__len__() > 0:
            cur_node = q.pop(0)
            if cur_node == 'end': 
                if cur_cnt:
                    avg = (cur_sum / cur_cnt)
                    ret.append(avg)
                cur_cnt, cur_sum = 0, 0.
                if q.__len__() == 0:
                    break
                q.append('end')
                continue
            cur_sum += cur_node.val
            cur_cnt += 1
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        return ret