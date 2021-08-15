class Tree():
    # 定义树节点，l, r, val表示该节点记录的是区间[l, r]的最大值是val
    def __init__(self):
        self.l = 0
        self.r = 0
        self.lazy = 0
        self.val = 0


class SegmentTree():
    def __init__(self):
        # 二叉树是堆形式，可以用一维数组存储，注意数组长度要开4倍空间
        self.tree = [Tree() for i in range(10*4)]

    def build(self, cur, l, r):
        # 建树，用 cur<<1 访问左子树，cur<<1|1 访问右子树，位运算操作很方便
        self.tree[cur].l, self.tree[cur].r, = l, r 
        self.tree[cur].lazy, self.tree[cur].val = 0, 0
        # 当 l == r 的时候结束递归
        if l < r:
            mid = l + r >> 1
            self.build(cur<<1, l, mid)
            self.build(cur<<1|1, mid+1, r)

    def pushup(self, cur):
        # 当子节点计算完成后，用子节点的值来更新自己的值
        self.tree[cur].val = max(self.tree[cur<<1].val, self.tree[cur<<1|1].val)    

    def add(self, cur, x, v):
        # 单点更新
        if self.tree[cur].l == self.tree[cur].r:
            self.tree[cur].val += v
        else:
            mid = self.tree[cur].r + self.tree[cur].l >> 1
            if x > mid:
                self.add(cur>>1|1, x, v)
            else:
                self.add(cur<<1, x, v)
            self.pushup(cur)

    def pushdown(self, cur):
        # 将lazy标记向下传递一层
        if self.tree[cur].lazy:
            lazy = self.tree[cur].lazy
            self.tree[cur<<1].lazy += lazy
            self.tree[cur<<1|1].lazy += lazy
            self.tree[cur<<1].val += lazy
            self.tree[cur<<1|1].val += lazy
            self.tree[cur].lazy = 0

    def update(self, cur, l, r, v):
        # 区间更新
        if l <= self.tree[cur].l and self.tree[cur].r <= r:
            self.tree[cur].lazy += v
            self.tree[cur].val += v
            return
        if r < self.tree[cur].l or l > self.tree[cur].r:
            return
        if self.tree[cur].lazy:
            self.pushdown(cur)
        self.update(cur<<1, l, r, v)
        self.update(cur<<1|1, l, r, v)
        self.pushup(cur)

    def query(self, cur, l=None, r=None):
        # 区间查询
        if l <= self.tree[cur].l and self.tree[cur].r <= r:
            return self.tree[cur].val
        if self.tree[cur].l > r or self.tree[cur].r < l:
            return 0
        if self.tree[cur].lazy:
            self.pushdown(cur)
        return max(self.query(cur<<1, l, r), self.query(cur<<1|1))


def test_segment_tree():
    # 测试
    # -----
    #        ---
    #  -------
    #   --
    #         --
    st = SegmentTree()
    st.build(1, 1, 10)
    st.update(1, 1, 5, 1)
    st.update(1, 7, 10, 1)
    st.update(1, 2, 8, 1)
    st.update(1, 3, 4, 1)
    st.update(1, 9, 10, 1)
    print(st.query(1, 1, 10))


if __name__ == "__main__":
    test_segment_tree()
