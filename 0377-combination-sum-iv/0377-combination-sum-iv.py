class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def find(s):
            if s == target:
                return 1
            if s in mem:
                return mem[s]
            cs = 0
            for i in range(len(nums)):
                if s+nums[i] <= target:
                    cs += find(s+nums[i])
            mem[s] = cs
            return cs
        
        mem = {}
        return find(0)
        