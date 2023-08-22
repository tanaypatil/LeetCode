class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        smap = {0:1}
        ans = s = 0
        for num in nums:
            s += num
            if s%k in smap:
                ans += smap[s%k]
            smap[s%k] = smap.get(s%k, 0) + 1
        return ans