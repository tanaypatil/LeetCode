from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if not s:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return ans