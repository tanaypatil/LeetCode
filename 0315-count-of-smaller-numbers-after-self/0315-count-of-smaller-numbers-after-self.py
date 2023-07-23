class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        sorted_rev = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            index = bisect_left(sorted_rev, nums[i])
            res[i] += index
            sorted_rev.insert(index, nums[i])
        return res