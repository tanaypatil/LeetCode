class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0: 1}
        s = 0
        c = 0
        for i, a in enumerate(nums):
            s += a
            if s-k in hm:
                c += hm[s-k]
            hm[s] = hm.get(s, 0) + 1
        return c
        