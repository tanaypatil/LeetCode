class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        
        def perm(mask, curr):
            if mask == (1<<n)-1:
                ans.add(tuple(curr))
                return
            
            for i in range(n):
                if not (mask & (1<<i)):
                    perm(mask|1<<i, curr+[nums[i]])
        
        perm(0, [])
        return ans
        