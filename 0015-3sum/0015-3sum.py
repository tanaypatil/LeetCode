from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            j, k = i + 1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if not s:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return result