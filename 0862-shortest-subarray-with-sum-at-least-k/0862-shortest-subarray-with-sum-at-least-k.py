class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_sums, cum_sum = deque({(0, -1)}), 0
        ans = float('inf')
        for i, num in enumerate(nums):
            cum_sum += num
            p = max(bisect_left(min_sums, (cum_sum-k, -1))-1, 0)
            while 0 <= p < len(min_sums) and cum_sum - min_sums[p][0] >= k:
                ans = min(ans, i-min_sums[p][1])
                p += 1
            while min_sums and cum_sum <= min_sums[-1][0]:
                min_sums.pop()
            min_sums.append((cum_sum, i))
        return ans if ans != float('inf') else -1