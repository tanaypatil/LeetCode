class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        smap = {0:1}
        s, ans = 0, 0
        for num in nums:
            s += num
            if s-k in smap:
                ans += smap[s-k]
            smap[s] = smap.get(s, 0) + 1
        return ans
        