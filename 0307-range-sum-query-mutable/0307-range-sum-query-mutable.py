class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(2*n)
        
    def build(self, nums):
        self.tree[self.n:] = nums
        for i in range(self.n-1, -1, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    def query(self, l, r):
        l += self.n
        r += self.n
        if l > r: return -1
        s = 0
        while l <= r:
            if l & 1:
                s += self.tree[l]
                l += 1
            if not (r & 1):
                s += self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return s


class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(len(nums))
        self.segment_tree.build(nums)

    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)