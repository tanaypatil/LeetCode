class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        smap = {0:1}
        ans = s = 0
        for num in nums:
            s += num
            if s-goal in smap:
                ans += smap[s-goal]
            smap[s] = smap.get(s, 0) + 1
        return ans
        