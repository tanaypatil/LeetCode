class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        
        i = j = k = l = 0
        n = len(nums)
        ret = set()
        for i in range(n-3):
            for l in range(n-1, i, -1):
                j = i + 1
                k = l - 1
                while j < k:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        ret.add((nums[i], nums[j], nums[k], nums[l]))
                        j += 1
                        k -= 1
                    elif s < target:
                        j += 1
                    else:
                        k -= 1
        return ret