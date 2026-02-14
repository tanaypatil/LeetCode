class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        doubles = [2*nums[-1]]
        ans = 0
        for i in range(len(nums)-2, -1, -1):
            ans += bisect_left(doubles, nums[i])
            doubles.insert(bisect_left(doubles, 2*nums[i]), 2*nums[i])
        return ans