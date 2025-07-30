class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            ans = l = 0
            counts = Counter()
            for r in range(len(nums)):
                if not counts[nums[r]]:
                    k -= 1
                counts[nums[r]] += 1
                while k < 0:
                    counts[nums[l]] -= 1
                    if not counts[nums[l]]:
                        k += 1
                    l += 1
                ans += (r-l+1)
            return ans

        return atMost(k) - atMost(k-1)
        