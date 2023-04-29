class Solution:
    def minRefuelStops(self, target: int, cur: int, s: List[List[int]]) -> int:
        pq = []
        res = i = 0
        while cur < target:
            while i < len(s) and s[i][0] <= cur:
                heapq.heappush(pq, -s[i][1])
                i += 1
            if not pq: return -1
            cur += -heapq.heappop(pq)
            res += 1
        return res
        