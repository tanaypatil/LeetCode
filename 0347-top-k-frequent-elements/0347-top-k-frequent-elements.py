from collections import Counter
from heapq import heapify, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        num_counts = [(-freq, num) for num, freq in counts.items()]
        heapify(num_counts)
        res = []
        for i in range(k):
            res.append(heappop(num_counts)[1])
        return res