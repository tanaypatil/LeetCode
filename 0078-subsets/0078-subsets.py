def genStr(s, t, res, i):
    if i >= len(s):
        return
    res.append(t+[s[i]])
    genStr(s, t+[s[i]], res, i+1)
    genStr(s, t, res, i+1)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        genStr(nums, [], res, 0)
        return res