class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)-x
        if not s:
            return len(nums)
        cs = 0
        smap = {}
        max_len = 0
        for i, num in enumerate(nums):
            cs += num
            if cs == s:
                max_len = i+1
            elif num == s:
                max_len = max(max_len, 1)
            elif cs-s in smap:
                max_len = max(max_len, i-smap[cs-s])
            if cs not in smap:
                smap[cs] = i
        if not max_len or max_len == len(nums):
            return -1
        
        return len(nums)-max_len
        
        