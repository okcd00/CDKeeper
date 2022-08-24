from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    序列化是将一个数据结构或者对象转换为连续的比特位的操作，
    进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，
    采取相反方式重构得到原数据。
    请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
    只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
    """
    def serialize_bfs(self, root):
        if not root:
            return ""
        dq = deque([root])
        res = []
        while dq:
            node = dq.popleft()
            if node:
                res.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                res.append('None')
        return ','.join(res)

    def deserialize_bfs(self, data):
        if not data:
            return []
        dataList = data.split(',')
        root = TreeNode(int(dataList[0]))
        dq = deque([root])
        i = 1
        while dq:
            node = dq.popleft()
            if dataList[i] != 'None':
                node.left = TreeNode(int(dataList[i]))
                dq.append(node.left)
            i += 1
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                dq.append(node.right)
            i += 1
        return root

    def serialize_dfs(self, root):
        if not root:
            return 'None'
        root.left = self.serialize(root.left)
        root.right = self.serialize(root.right)
        return f"{root.val},{root.left},{root.right}"

    def deserialize_dfs(self, data):
        dq = deque(data.split(','))

        def dfs(li):
            val = li.popleft()
            if val == "None":
                return None
            root = TreeNode(int(val))
            root.left = dfs(li)
            root.right = dfs(li)
            return root
        return dfs(dq)


if __name__ == "__main__":
    root = TreeNode(1)
    pass