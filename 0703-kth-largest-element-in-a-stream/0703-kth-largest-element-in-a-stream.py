from bisect import bisect_left
from heapq import heapify, heappush, heappop


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # self.nums = list(sorted(nums))
        heapify(nums)
        self.nums = nums
        while len(self.nums) > k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        # i = bisect_left(self.nums, val)
        # self.nums.insert(i, val)
        # n = len(self.nums)
        # # print(self.nums)
        # return self.nums[-self.k]
        if len(self.nums) == self.k and val > self.nums[0]:
            heappush(self.nums, val)
            heappop(self.nums)
        elif len(self.nums) < self.k:
            heappush(self.nums, val)
        # print(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)