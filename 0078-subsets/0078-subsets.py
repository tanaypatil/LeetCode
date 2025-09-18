class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2**(len(nums))):
            bs = bin(i)[2:]
            bs = "0"*(len(nums)-len(bs)) + bs
            curr = []
            for p, j in enumerate(bs):
                if j != "0":
                    curr.append(nums[p])
            res.append(curr)
        return res