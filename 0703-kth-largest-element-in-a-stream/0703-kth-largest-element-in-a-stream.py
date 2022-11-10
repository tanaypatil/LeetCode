from bisect import bisect_left


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = list(sorted(nums))

    def add(self, val: int) -> int:
        i = bisect_left(self.nums, val)
        self.nums.insert(i, val)
        n = len(self.nums)
        # print(self.nums)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)