class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, ans = 0, 0
        for num in nums:
            if num:
                count += num
            else:
                ans = max(ans, count)
                count = 0
        return max(ans, count)
        