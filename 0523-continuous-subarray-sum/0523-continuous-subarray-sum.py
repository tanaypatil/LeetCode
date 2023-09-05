class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        smap = {0:-1}
        zeroes = 0
        for i, num in enumerate(nums):
            s += num
            if (s % k) in smap:
                if i-smap[s%k] >= 2: return True
            else: smap[s%k] = i
        return False