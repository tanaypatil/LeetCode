class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s, cs = sum(nums), 0
        ans = 0
        for i in range(len(nums)-1):
            cs += nums[i]
            if cs >= s-cs:
                ans += 1
        return ans