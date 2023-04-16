class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0: 1}
        s = c = 0
        for num in nums:
            s += num
            if s-k in hm:
                c += hm[s-k]
            hm[s] = hm.get(s, 0) + 1
        return c
        