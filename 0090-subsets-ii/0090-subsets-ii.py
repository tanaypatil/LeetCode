def genSets(arr, index, res, path):
    if index >= len(arr):
        return
    res.add(tuple(path+[arr[index]]))
    genSets(arr, index+1, res, path+[arr[index]])
    genSets(arr, index+1, res, path)

    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        genSets(nums, 0, res, [])
        res.add(tuple([]))
        return res